from noise_campaign.histogram_bin import HistogramBin

class Histogram:
    def __init__(
        self,
        wind_speed_min: int,
        wind_speed_max: int,
        wind_speed_bin_size: int,
        wind_direction_min: int,
        wind_direction_max: int,
        wind_direction_bin_size: int):

        self.bins = []
        for x in range(wind_speed_min,wind_speed_max, wind_speed_bin_size):
            for y in range(wind_direction_min, wind_direction_max, wind_direction_bin_size):
                wind_speed_bin_start = x
                wind_speed_bin_end = wind_speed_bin_start + wind_speed_bin_size
                wind_direction_bin_start = y 
                wind_direction_bin_end = wind_direction_bin_start + wind_direction_bin_size

                new_bin = HistogramBin(
                    wind_speed_bin_start,
                    wind_speed_bin_end,
                    wind_direction_bin_start,
                    wind_direction_bin_end)

                self.bins.append(new_bin)

    def get_bins_list(self):
        return self.bins
    def get_incomplete_bins(self):
        incomplete_bins = []
        for histogram_bin in self.bins:
            if histogram_bin.has_missing_measurements:
                incomplete_bins.append(histogram_bin)
        return incomplete_bins

    
    def get_correct_bin(self, wind_speed, wind_direction):
        for histogram_bin in self.bins:
            if histogram_bin.can_store_measurement(wind_speed, wind_direction):
                return histogram_bin


if __name__ == '__main__':
    h = Histogram(0, 1, 1, 0, 1, 1)
    #b = h.get_correct_bin(11,120)
    #print(b.wind_speed_range, b.wind_direction_range)
    for b in h.get_bins_list():
        print(b.wind_speed_range, b.wind_direction_range)

