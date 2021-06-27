import os
from flask import Flask, jsonify, request
from noise_campaign.measured_state import MeasuredState
from noise_campaign.data_handler import DataHandler
from noise_campaign.init_database import init_db
from noise_campaign.histogram import Histogram
import noise_campaign.noise_campaign_helper as nch
import datetime as dt

app = Flask(__name__)
db_client = init_db()


@app.route("/turbineStatus", methods=["POST"])
def get_turbine_status():
    histogram = Histogram(
        int(os.getenv("CENTER_OF_FIRST_WIND_SPEED_BIN")),
        int(os.getenv("NUMBER_OF_WIND_SPEED_BINS")),
        int(os.getenv("WIND_SPEED_BIN_WIDTH")),
        int(os.getenv("NUMBER_OF_WIND_DIRECTION_BINS")),
    )
    campaign_start_time = dt.datetime.strptime(
        os.getenv("CAMPAIGN_START_TIME"), "%Y-%m-%d %H:%M:%S%z"
    )

    data_handler = DataHandler(db_client)
    measured_state = MeasuredState(histogram, request.json)
    status = measured_state.status
    last_sample_time = measured_state.timestamp

    if not nch.downsampled_sample_exits(data_handler):
        nch.build_first_sample(
            last_sample_time,
            campaign_start_time,
            data_handler,
            histogram,
            status,
            measured_state,
        )
    else:
        if nch.sample_is_from_previous_period(last_sample_time, data_handler):
            return jsonify(create_response(status, request, dt.datetime.now()))
        elif nch.sample_is_from_new_period(last_sample_time, data_handler):
            data_handler.write_measured_state(measured_state)
        else:
            aggregated_timestamp = nch.downsample_30s_samples(
                data_handler, status, histogram
            )
            aggregate_samples_size = data_handler.get_10min_observed_data_size()
            if aggregate_samples_size >= int(os.getenv("SEED_TRAINING_SET_SIZE")):
                status = get_required_status(
                    data_handler, aggregated_timestamp, histogram
                )

    return jsonify(create_response(status, request, dt.datetime.now()))


def get_required_status(data_handler, aggregated_timestamp, histogram):
    training_set = data_handler.get_training_set(os.getenv("SEED_TRAINING_SET_SIZE"))
    predicted_state = nch.get_predicted_state(
        training_set, histogram, aggregated_timestamp, data_handler
    )
    data_handler.write_predicted_state(predicted_state)
    status = predicted_state.turbine_status
    return status


def create_response(status, request, timestamp):
    data_dict = request.json
    response_dict = {"turbines": []}
    turbines = data_dict["turbines"]
    for turbine in turbines:
        turbine_dict = {
            "id": turbine["id"],
            "requiredRunState": status,
            "timestampUTC": timestamp,
        }
        response_dict["turbines"].append(turbine_dict)
    return response_dict


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.getenv("API_PORT"))
