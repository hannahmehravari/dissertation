from noise_campaign.measured_state import MeasuredState


class DataHandler:
    def __init__(self, db_client):
        self.db_client = db_client

    def write_measured_state(self, measured_state: MeasuredState):
        self.db_client.create_database("observed_data")
        self.db_client.switch_database("observed_data")

        point_dict = {}
        point_dict["measurement"] = '30s_sample'
        point_dict["time"] = measured_state.timestamp
        point_dict["fields"] = {"wind_speed": measured_state.average_wind_speed,
                                "wind_direction": measured_state.average_wind_direction}

        self.db_client.write_points([point_dict])

    def write_prediction(self, prediction):
        return None

    def get_prediction(self, timestamp):
        return None

    def get_training_set(self, training_set_size):
        return None
