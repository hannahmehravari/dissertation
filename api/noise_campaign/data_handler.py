from noise_campaign.measured_state import MeasuredState
from noise_campaign.predicted_state import PredictedState
import pandas as pd
import datetime as dt


class DataHandler:
    def __init__(self, db_client):
        self.db_client = db_client

    def write_measured_state(self, measured_state: MeasuredState):
        self.db_client.switch_database("30s_observed_data")
        point_dict = {
            measured_state.timestamp: [
                measured_state.average_wind_speed,
                measured_state.average_wind_direction,
            ]
        }
        columns = ["wind_speed", "wind_direction"]
        point_df = pd.DataFrame.from_dict(
            data=point_dict, orient="index", columns=columns
        )
        point_df.index.rename("time", inplace=True)

        self.db_client.write_points(
            point_df,
            "30s_sample",
            {
                "wind_speed_bin": measured_state.wind_speed_bin,
                "wind_direction_bin": measured_state.wind_direction_bin,
                "run_state" : measured_state.status
            },
        )

    def write_predicted_state(self, predicted_state: PredictedState):

        self.db_client.switch_database("predicted_data")

        point_dict = {
            predicted_state.timestamp: [
                predicted_state.average_wind_speed,
                predicted_state.average_wind_direction,
            ]
        }

        columns = [
            "wind_speed",
            "wind_direction",
        ]

        point_df = pd.DataFrame.from_dict(
            data=point_dict, orient="index", columns=columns
        )
        point_df.index.rename("time", inplace=True)
        self.db_client.write_points(
            point_df,
            "prediction",
            {
                "wind_speed_bin": predicted_state.wind_speed_bin,
                "wind_direction_bin": predicted_state.wind_direction_bin,
            },
        )


    def write_aggregated_state(self, wind_speed, wind_direction, wind_speed_bin, wind_direction_bin, turbine_status, timestamp):
        self.db_client.switch_database("10min_observed_data")
        point_dict = {
            timestamp: [
                wind_speed,
                wind_direction,
            ]
        }
        columns = ["wind_speed", "wind_direction"]
        point_df = pd.DataFrame.from_dict(
            data=point_dict, orient="index", columns=columns
        )
        point_df.index.rename("time", inplace=True)

        self.db_client.write_points(
            point_df,
            "10min_sample",
            {
                "wind_speed_bin": wind_speed_bin,
                "wind_direction_bin": wind_direction_bin,
                "run_state" : turbine_status
            },
        )

    def get_prediction(self, timestamp):
        return None

    def get_training_set(self, training_set_size):
        print(training_set_size)
        self.db_client.switch_database("10min_observed_data")
        result = self.db_client.query(
            f'SELECT * FROM "10min_sample" ORDER BY desc LIMIT {training_set_size}'
        )
        return result['10min_sample']

    def get_latest_samples(self, size):
        self.db_client.switch_database("30s_observed_data")
        result = self.db_client.query(
            f'SELECT * FROM "30s_sample" ORDER BY desc LIMIT {int(size)}'
        )

        return result['30s_sample']

    def get_10min_observed_data_size(self):
        self.db_client.switch_database("10min_observed_data")
        result = self.db_client.query(
            'SELECT COUNT("wind_speed") FROM "10min_sample"'
        )

        return result['10min_sample']['count'][0]

    def get_30s_observed_data_size(self):
        self.db_client.switch_database("30s_observed_data")
        result = self.db_client.query(
            'SELECT COUNT("wind_speed") FROM "30s_sample"'
        )

        return result['30s_sample']['count'][0]

    def get_number_of_measurements_by_bin_and_status(self, speed_bin, direction_bin, status):
        self.db_client.switch_database("10min_observed_data")
        result = self.db_client.query(f"SELECT COUNT(wind_speed) FROM \"10min_sample\" WHERE wind_speed_bin=\'{speed_bin}\' AND wind_direction_bin=\'{direction_bin}\' AND run_state=\'{status}\'")
        print(result)

        if len(result) == 0:
            return 0
        else:
            return result['10min_sample']['count'][0]

    def clear_30s_measurements(self):
        self.db_client.switch_database("30s_observed_data")
        self.db_client.query('DROP SERIES FROM "30s_sample"')
