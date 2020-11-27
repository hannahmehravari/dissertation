from noise_campaign.histogram_bin import HistogramBin

class Histogram:
    def __init__(
        self,
        wind_speed_min: int,
        wind_speed_max: int,
        wind_speed_bin_count: int,
        wind_direction_min: int,
        wind_direction_max: int,
        wind_direction_bin_count: int):

        wind_speed_bin_size = (wind_speed_max - wind_speed_min) / float(wind_speed_bin_count)
        wind_direction_bin_size = (wind_direction_max - wind_direction_min) / float(wind_direction_bin_count)

        self.bins = []
        for x in range(0, wind_speed_bin_count):
            for y in range(0, wind_direction_bin_count):
            wind_speed_bin_start = wind_speed_min + x * wind_speed_bin_size
            wind_speed_bin_end = wind_speed_bin_start + wind_speed_bin_size
            wind_direction_bin_start = wind_direction_min + y * wind_direction_bin_size
            wind_direction_bin_end = wind_direction_bin_start + wind_direction_bin_count

            new_bin = HistogramBin(
                wind_speed_bin_start,
                wind_speed_bin_end,
                wind_direction_bin_start,
                wind_direction_bin_end)

            self.bins.append(new_bin)

    
    def get_incomplete_bins(self):
        incomplete_bins = []
        for histogram_bin in bins:
            if histogram_bin.has_missing_measurements:
                incomplete_bins.append(histogram_bin)
        return incomplete_bins

    
    def insert_measurement(self, wind_speed, wind_direction, turbine_status, noise_measurement):
        for histogram_bin in bins:
            if histogram_bin.can_store_measurement(wind_speed, wind_direction):
                histogram_bin.set_measurement(turbine_status, noise_measurement)


