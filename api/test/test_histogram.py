from noise_campaign.histogram import Histogram
histogram = Histogram()

def test_histogram_bins_creation_speed():
    histogram = Histogram()
    actual_bins = histogram.get_wind_speed_bins(0, 2, 1)
    expected_bins = {0: [-0.5, 0.5], 1: [0.5, 1.5]}
    assert expected_bins == actual_bins


def test_histogram_bins_creation_direction():
    actual_bins = histogram.get_wind_direction_bins(12)
    expected_bins = {
        0.0: [-15.0, 15.0],
        30.0: [15.0, 45.0],
        60.0: [45.0, 75.0],
        90.0: [75.0, 105.0],
        120.0: [105.0, 135.0],
        150.0: [135.0, 165.0],
        180.0: [165.0, 195.0],
        210.0: [195.0, 225.0],
        240.0: [225.0, 255.0],
        270.0: [255.0, 285.0],
        300.0: [285.0, 315.0],
        330.0: [315.0, 345.0],
    }

    assert expected_bins == actual_bins
