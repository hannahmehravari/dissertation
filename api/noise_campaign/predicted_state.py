class PredictedState:
    def __init__(self, histogram, average_wind_speed, average_wind_direction, timestamp):
        self.average_wind_speed = average_wind_speed
        self.average_wind_direction = average_wind_direction
        self.timestamp = timestamp

        self.wind_speed_bin = histogram.get_wind_speed_bin(self.average_wind_speed)
        self.wind_direction_bin = histogram.get_wind_direction_bin(self.average_wind_direction)



    
    