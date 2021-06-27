import datetime as dt
from noise_campaign.predicted_state import PredictedState
from noise_campaign.prediction_maker import PredictionMaker
import os 

def downsampled_sample_exits(data_handler):
    return data_handler.get_last_timestamp_in_10_minute_measurement() is not None

def sample_is_from_previous_period(last_sample_time, data_handler):
    time_diff = last_sample_time - data_handler.get_last_timestamp_in_10_minute_measurement()
    return (time_diff).total_seconds() <= 0

def sample_is_from_new_period(last_sample_time, data_handler):
    time_diff = last_sample_time - data_handler.get_last_timestamp_in_10_minute_measurement()
    return (time_diff < dt.timedelta(minutes=8) and time_diff.total_seconds() > 0)

def downsample_30s_samples(data_handler, status, histogram):
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

    return aggregated_timestamp


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

def build_first_sample(last_sample_time, campaign_start_time, data_handler, histogram, status, measured_state):
    if (last_sample_time - campaign_start_time) <= dt.timedelta(minutes=8):
        data_handler.write_measured_state(measured_state)
    else:
        aggregated_timestamp = downsample_30s_samples(
            data_handler, status, histogram
        )
