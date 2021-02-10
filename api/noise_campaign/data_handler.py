from noise_campaign.measured_state import MeasuredState

class DataHandler:

    def __init__(self, db_client):
        self.db_client = db_client


    def write_measured_state(self, measured_state: MeasuredState):

        self.db_client.switch_database('vardafjellet')
        json_body = [
                {
                    "measurement": "wind_speed",
                    "tags": {},
                    "time": measured_state.timestamp,
                    "fields": {
                        "value": measured_state.average_wind_speed
                    }
                }
            ]
        self.db_client.write_points(json_body)

    def write_prediction(self, prediction):
        return None

    def get_prediction(self, timestamp):
        return None

    def get_training_set(self, training_set_size):
        return None

    

