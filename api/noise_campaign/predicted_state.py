import pytz

class PredictedState:
    def __init__(self, histogram, average_wind_speed, average_wind_direction, timestamp):
        self.average_wind_speed = average_wind_speed
        self.average_wind_direction = average_wind_direction
        self.timestamp = timestamp
        self.timestamp.tz_convert('UTC')
        self.wind_speed_bin = histogram.get_wind_speed_bin(self.average_wind_speed)
        self.wind_direction_bin = histogram.get_wind_direction_bin(self.average_wind_direction)
        self.turbine_status = None
    

    def set_turbine_status(self, status):
        self.turbine_status = status



    
    