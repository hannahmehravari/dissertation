from noise_campaign.measured_state import MeasuredState
from noise_campaign.predicted_state import PredictedState

class DataHandler:
    def __init__(self, db_client):
        self.db_client = db_client

    def write_measured_state(self, measured_state: MeasuredState):
        self.db_client.switch_database("observed_data")

        point_dict = {}
        point_dict["measurement"] = "30s_sample"
        point_dict["time"] = measured_state.timestamp
        point_dict["fields"] = {
            "wind_speed": measured_state.average_wind_speed,
            "wind_direction": measured_state.average_wind_direction,
            "speed_bin" : measured_state.speed_bin,
            "direction_bin" : measured_state.direction_bin
        }

        self.db_client.write_points([point_dict])

    def write_predicted_state(
        self,
        predicted_state : PredictedState
    ):
        self.db_client.switch_database("predicted_data")
        point_dict = {}
        point_dict["measurement"] = "prediction"
        point_dict["time"] = predicted_state.timestamp
        point_dict["fields"] = {
            "wind_speed": predicted_state.average_wind_speed,
            "wind_direction": predicted_state.average_wind_direction,
            "wind_speed_bin" : predicted_state.wind_speed_bin,
            "wind_direction_bin" : predicted_state.wind_direction_bin
        }
        
        self.db_client.write_points([point_dict])

    def get_prediction(self, timestamp):
        return None

    def get_training_set(self, training_set_size):
        return None

    def get_observed_data_size():
        self.db_client.switch_database("observed_data")
        result = self.db_client.query(
            'SELECT COUNT("mean_wind_speed") FROM (select *  from "observed_data"."1_week"."2min_sample" fill(0))'
        )
        return result

