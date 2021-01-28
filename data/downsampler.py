class Downsampler:
    def __init__(self):
        pass

    def downsample(self, high_freq_data, required_freq='2min', time_stamp_column_name):
        averaged_over_turbines = self.average_over_turbines(high_freq_data, time_stamp_column_name)
        downsampled = self.resample(averaged_over_turbines, required_freq)
        return downsampled

    def resample(self, high_freq_data, required_freq)
        resampled = high_freq_data.resample(required_freq).mean()
        return resampled.asfreq(pd.infer_freq(data_rs.index))

    def average_over_turbines(self, high_freq_data, time_stamp_column_name):
        return data.groupby([time_stamp_column_name]).mean()

