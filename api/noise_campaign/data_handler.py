from noise_campaign.measured_state import MeasuredState


class DataHandler:
    def __init__(self, db_client):
        self.db_client = db_client

    def write_measured_state(self, measured_state: MeasuredState):
        self.db_client.switch_database("vardafjellet")

        wind_speed = self._get_point_dict(
            "wind_speed", 
            measured_state.average_wind_speed,
            measured_state.timestamp
        )
        wind_direction = self._get_point_dict(
            "wind_direction",
            measured_state.average_wind_direction,
            measured_state.timestamp,
        )

        self.db_client.write_points([wind_speed, wind_direction])

    def write_prediction(self, prediction):
        return None

    def get_prediction(self, timestamp):
        return None

    def get_training_set(self, training_set_size):
        return None

    def _get_point_dict(self, measurement_name, value, timestamp):
        point_dict = {}
        point_dict["measurement"] = measurement_name
        point_dict["time"] = timestamp
        point_dict["fields"] = {"value": value}
        return point_dict

