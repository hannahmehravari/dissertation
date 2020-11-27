class HistogramBin:
    def __init__(
        self,
        bin_wind_speed_start,
        bin_wind_speed_end,
        bin_wind_direction_start,
        bin_wind_direction_end):

        self.wind_speed_range = range(bin_wind_speed_start, bin_wind_speed_end)
        self.wind_direction_range = range(bin_wind_direction_start, bin_wind_direction_end)

        self.measurement_with_turbine_running = None
        self.measurement_with_turbine_paused = None

    def has_missing_running_measurement(self):
        return self.measurement_with_turbine_running is None

    def has_missing_paused_measurement(self):
        return self.measurement_with_turbine_paused is None

    def has_missing_measurements(self):
        if self.has_missing_paused_measurement or self.has_missing_running_measurement:
            return True 
        return False

    def set_measurement(
        self,
        turbine_status: TurbineStatus,
        noise_measurement: float)

        if turbine_status == TurbineStatus.RUNNING:
            self.measurement_with_turbine_running = noise_measurement
        elif turbine_status == TurbineStatus.PAUSED:
            self.measurement_with_turbine_paused = noise_measurement

    def can_store_measurement(
        self,
        wind_speed: float,
        wind_direction: float):
        return (wind_speed in self.wind_speed_range and wind_direction in self.wind_direction_range)