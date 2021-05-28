from noise_campaign.histogram import Histogram
class PredictedState:
    def __init__(self, average_wind_speed, average_wind_direction, timestamp):
        self.average_wind_speed = average_wind_speed
        self.average_wind_direction = average_wind_direction
        self.timestamp = timestamp

        self.wind_speed_bin = None
        self.wind_direction_bin = None



    
    