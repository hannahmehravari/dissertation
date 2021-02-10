import numpy as np

class Histogram:
    def __init__(self):
        pass

    def get_wind_speed_bins(self, center_of_first_bin, number_of_bins, bin_width):
        center_of_last_bin = (
            number_of_bins * bin_width - bin_width + center_of_first_bin
        )
        bin_centers = np.arange(
            start=center_of_first_bin,
            stop=center_of_last_bin + bin_width,
            step=bin_width,
        )
        bins = {}
        for center in bin_centers:
            bins[center] = self._create_bin_interval(center, bin_width)
        return bins

    def get_wind_direction_bins(self, number_of_bins):
        bin_width = 360.0 / number_of_bins
        bin_centers = np.arange(0.0, 360.0, bin_width)
        bin_edges = np.arange(start=0.0 - bin_width / 2, stop=360.0, step=bin_width)
        bins = {}
        for bin_center in bin_centers:
            bins[bin_center] = self._create_bin_interval(bin_center, bin_width)
        return bins

    def _create_bin_interval(self, bin_center, bin_width):
        lower_bin_limit = bin_center - (bin_width / 2.0)
        upper_bin_limit = bin_center + (bin_width / 2.0)
        return [lower_bin_limit, upper_bin_limit]


if __name__ == "__main__":
    h = Histogram()
    # i = h.get_wind_speed_bins(0, 2, 1)
    # print(i)
    i = h.get_wind_direction_bins(12)
    print(i)

