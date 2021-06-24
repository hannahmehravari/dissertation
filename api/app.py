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

app = Flask(__name__)
db_client = init_db()


@app.route("/turbineStatus", methods=["POST"])
def get_turbine_status():

    histogram = Histogram(3, 12, 1, 12)
    data_handler = DataHandler(db_client)

    measured_state = MeasuredState(histogram, request.json)
    data_handler.write_measured_state(measured_state)
    status=measured_state.status
    last_sample_time=measured_state.timestamp

    latest_samples_size = data_handler.get_30s_observed_data_size()
    print(latest_samples_size)

    if latest_samples_size < 16:
        data_handler.write_measured_state(measured_state)
    elif latest_samples_size >= 16:
        latest_samples = data_handler.get_latest_samples(16)

        aggregate_wind_speed = latest_samples["wind_speed"].mean()
        aggregate_wind_speed_bin = histogram.get_wind_speed_bin(aggregate_wind_speed)
        aggregate_wind_direction = latest_samples["wind_direction"].mean()
        aggregate_wind_direction_bin = histogram.get_wind_direction_bin(
            aggregate_wind_direction
        )
        data_handler.clear_30s_measurements()

        aggregated_timestamp = last_sample_time + dt.timedelta(minutes=2)

        data_handler.write_aggregated_state(
            aggregate_wind_speed,
            aggregate_wind_direction,
            aggregate_wind_speed_bin,
            aggregate_wind_direction_bin,
            status,
            aggregated_timestamp
        )

        aggregate_samples_size = data_handler.get_10min_observed_data_size()

        print(aggregate_samples_size)

        if aggregate_samples_size >= int(os.getenv("SEED_TRAINING_SET_SIZE")):

          training_set = data_handler.get_training_set(os.getenv("SEED_TRAINING_SET_SIZE"))
          print(training_set)

          predicted_state = get_predicted_state(training_set, histogram)
          data_handler.write_predicted_state(predicted_state)

          predicted_bin_stop_count = data_handler.get_number_of_measurements_by_bin_and_status(
              predicted_state.wind_speed_bin, predicted_state.wind_direction_bin, "Paused"
          )
          predicted_bin_run_count = data_handler.get_number_of_measurements_by_bin_and_status(
              predicted_state.wind_speed_bin, predicted_state.wind_direction_bin, "Started"
          )

          if predicted_bin_stop_count < int(os.getenv("MIN_COUNTS_REQUIRED")):
              status = "Paused"
          elif predicted_bin_run_count < int(os.getenv("MIN_COUNTS_REQUIRED")):
              status = "Started"
          else:
              status = "Started"

          print(status)

    return jsonify(
        {
            "state" : status,
        }
    )



def get_predicted_state(training_set, histogram, last_observed_time):
    prediction_maker = PredictionMaker()

    print(training_set["wind_direction"])
    direction_prediction = prediction_maker.make_prediction(
        training_set["wind_direction"]
    )
    speed_prediction = prediction_maker.make_prediction(
        training_set["wind_speed"]
    )
    return PredictedState(
        histogram, speed_prediction, direction_prediction, last_observed_time + dt.timedelta(minutes=10)
    )


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
