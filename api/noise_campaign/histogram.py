import numpy as np

class Histogram:
    def __init__(
        self,
        center_of_first_speed_bin,
        number_of_speed_bins,
        speed_bin_width,
        number_of_direction_bins,
    ):
        self.center_of_first_speed_bin = center_of_first_speed_bin
        self.number_of_speed_bins = number_of_speed_bins
        self.speed_bin_width = speed_bin_width
        self.number_of_direction_bins = number_of_direction_bins

        self.speed_bins = self._create_wind_speed_bins()
        self.direction_bins = self._create_wind_direction_bins()


    def get_bin_for_state(self, state):
        return None

    def get_wind_speed_bin(self, wind_speed):
        wind_speed = float(wind_speed)
        for bin in self.speed_bins.keys():
            edges = self.speed_bins[bin]
            if (wind_speed > edges[0]) and  (wind_speed <= edges[1]):
                return bin
        
    def get_wind_direction_bin(self, wind_direction):
        if wind_direction >= 345:
            wind_direction = wind_direction - 360
        for bin in self.direction_bins.keys():
            edges = self.direction_bins[bin]
            if (wind_direction > edges[0]) and (wind_direction <= edges[1]):
                return bin
        
    def get_wind_speed_bins(self):
        return self.speed_bins

    def get_wind_direction_bins(self):
        return self.direction_bins

    def _create_wind_speed_bins(self):
        center_of_last_bin = (
            self.number_of_speed_bins * self.speed_bin_width
            - self.speed_bin_width
            + self.center_of_first_speed_bin
        )
        bin_centers = np.arange(
            start=self.center_of_first_speed_bin,
            stop=center_of_last_bin + self.speed_bin_width,
            step=self.speed_bin_width,
        )
        bins = {}
        for center in bin_centers:
            bins[center] = self._create_bin_interval(center, self.speed_bin_width)
        return bins

    def _create_wind_direction_bins(self):
        bin_width = 360.0 / self.number_of_direction_bins
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
