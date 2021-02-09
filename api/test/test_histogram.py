from noise_campaign.histogram import Histogram
from noise_campaign.histogram_bin import HistogramBin
def test_histogram_bins_creation_speed():
    histogram = Histogram(0, 1, 1, 0, 1, 1)

    actual_bins = histogram.get_bins_list()
    expected_bins = [HistogramBin(0,1,0,1)]

    assert expected_bins[0].wind_speed_range == actual_bins[0].wind_speed_range
    
def test_histogram_bins_creation_direction():
    histogram = Histogram(0, 1, 1, 0, 1, 1)

    actual_bins = histogram.get_bins_list()
    expected_bins = [HistogramBin(0,1,0,1)]

    assert expected_bins[0].wind_direction_range == actual_bins[0].wind_direction_range
    
