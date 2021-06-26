from noise_campaign.predicted_state import PredictedState
from noise_campaign.prediction_maker import PredictionMaker
import os
from flask import Flask, jsonify, request
import json
from noise_campaign.measured_state import MeasuredState
from noise_campaign.data_handler import DataHandler
from noise_campaign.init_database import init_db
from noise_campaign.histogram import Histogram
import pandas as pd
import datetime as dt
import pytz

app = Flask(__name__)
db_client = init_db()


@app.route("/turbineStatus", methods=["POST"])
def get_turbine_status():

    histogram = Histogram(3, 12, 1, 12)
    data_handler = DataHandler(db_client)

    measured_state = MeasuredState(histogram, request.json)
    data_handler.write_measured_state(measured_state)
    status = measured_state.status
    last_sample_time = measured_state.timestamp
    campaign_start_time = dt.datetime.strptime(
        os.getenv("CAMPAIGN_START_TIME"), "%Y-%m-%d %H:%M:%S%z"
    )

    if data_handler.get_last_timestamp_in_10_minute_measurement() is None:
        if (last_sample_time - campaign_start_time) <= dt.timedelta(minutes=8):
            data_handler.write_measured_state(measured_state)
        else:
            latest_samples = data_handler.get_latest_samples()
            aggregate_wind_speed = latest_samples["wind_speed"].mean()
            aggregate_wind_speed_bin = histogram.get_wind_speed_bin(
                aggregate_wind_speed
            )
            aggregate_wind_direction = latest_samples["wind_direction"].mean()
            aggregate_wind_direction_bin = histogram.get_wind_direction_bin(
                aggregate_wind_direction
            )
            aggregated_timestamp = data_handler.get_last_timestamp_in_30_second_measurement() + dt.timedelta(
                minutes=2
            )
            data_handler.clear_30s_measurements()
            data_handler.write_aggregated_state(
                aggregate_wind_speed,
                aggregate_wind_direction,
                aggregate_wind_speed_bin,
                aggregate_wind_direction_bin,
                status,
                aggregated_timestamp,
            )
    else:
        time_diff = last_sample_time - data_handler.get_last_timestamp_in_10_minute_measurement()
        if (time_diff).total_seconds() <= 0:
            print('here')
            return jsonify({"state": status,})
        elif time_diff < dt.timedelta(minutes=8) and time_diff.total_seconds() > 0:
            print('there')
            data_handler.write_measured_state(measured_state)
        else:
            latest_samples = data_handler.get_latest_samples()
            aggregate_wind_speed = latest_samples["wind_speed"].mean()
            aggregate_wind_speed_bin = histogram.get_wind_speed_bin(
                aggregate_wind_speed
            )
            aggregate_wind_direction = latest_samples["wind_direction"].mean()
            aggregate_wind_direction_bin = histogram.get_wind_direction_bin(
                aggregate_wind_direction
            )
            aggregated_timestamp = data_handler.get_last_timestamp_in_30_second_measurement() + dt.timedelta(
                minutes=2
            )
            data_handler.clear_30s_measurements()
            data_handler.write_aggregated_state(
                aggregate_wind_speed,
                aggregate_wind_direction,
                aggregate_wind_speed_bin,
                aggregate_wind_direction_bin,
                status,
                aggregated_timestamp,
            )
            aggregate_samples_size = data_handler.get_10min_observed_data_size()
            if aggregate_samples_size >= int(os.getenv("SEED_TRAINING_SET_SIZE")):
                training_set = data_handler.get_training_set(
                    os.getenv("SEED_TRAINING_SET_SIZE")
                )
                predicted_state = get_predicted_state(
                    training_set, histogram, aggregated_timestamp, data_handler
                )
                data_handler.write_predicted_state(predicted_state)
                status = predicted_state.turbine_status

    return jsonify({"state": status,})


def get_predicted_state(training_set, histogram, last_observed_time, data_handler):
    prediction_maker = PredictionMaker()

    direction_prediction = prediction_maker.make_prediction(
        training_set["wind_direction"]
    )
    speed_prediction = prediction_maker.make_prediction(training_set["wind_speed"])

    predicted_state = PredictedState(
        histogram,
        speed_prediction,
        direction_prediction,
        last_observed_time + dt.timedelta(minutes=10),
    )

    predicted_bin_stop_count = data_handler.get_number_of_measurements_by_bin_and_status(
        predicted_state.wind_speed_bin, predicted_state.wind_direction_bin, "Paused"
    )
    predicted_bin_run_count = data_handler.get_number_of_measurements_by_bin_and_status(
        predicted_state.wind_speed_bin, predicted_state.wind_direction_bin, "Started"
    )

    if predicted_bin_stop_count < int(os.getenv("MIN_COUNTS_REQUIRED")):
        predicted_state.set_turbine_status("Paused")
    elif predicted_bin_run_count < int(os.getenv("MIN_COUNTS_REQUIRED")):
        predicted_state.set_turbine_status("Started")
    else:
        predicted_state.set_turbine_status("Started")
    return predicted_state


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("API_PORT"))

"""
{
  ""turbines"":
    [
      {
        ""id"": ""Garreg Lywd.WTG01"",
        ""requiredRunState"": ""Started"",
        ""timestampUTC"": ""2018-10-16T12:01:00Z""
      },
      {
        ""id"": ""Garreg Lywd.WTG03"",
        ""requiredRunState"": ""Paused"",
        ""timestampUTC"": ""2018-10-16T12:01:35Z""
      },
      {
        ""id"": ""Garreg Lywd.WTG04"",
        ""requiredRunState"": ""Unknown"",
        ""timestampUTC"": ""2018-10-16T12:01:35Z""
      }
    ]
}
"""
