from noise_campaign.turbine_status import TurbineStatus

class HistogramBin:
    def __init__(
        self,
        bin_wind_speed_start,
        bin_wind_speed_end,
        bin_wind_direction_start,
        bin_wind_direction_end):

        self.wind_speed_range = range(int(bin_wind_speed_start), int(bin_wind_speed_end))
        self.wind_direction_range = range(int(bin_wind_direction_start), int(bin_wind_direction_end))

        self.measurement_with_turbine_running = None
        self.measurement_with_turbine_paused = None

    def can_store_measurement(
        self,
        wind_speed: float,
        wind_direction: float):
        return (wind_speed in self.wind_speed_range and wind_direction in self.wind_direction_range)