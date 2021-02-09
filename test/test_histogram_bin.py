from noise_campaign.histogram_bin import HistogramBin


def test_histogram_bin_wind_speed_bin_creation():
    histogram_bin = HistogramBin(
        bin_wind_speed_start=0,
        bin_wind_speed_end=5,
        bin_wind_direction_start=10,
        bin_wind_direction_end=15,
    )
    expected_wind_speed_range = range(0, 5)
    actual_wind_speed_range = histogram_bin.wind_speed_range
    assert expected_wind_speed_range == actual_wind_speed_range


def test_histogram_bin_wind_direction_bin_creation():
    histogram_bin = HistogramBin(
        bin_wind_speed_start=0,
        bin_wind_speed_end=5,
        bin_wind_direction_start=10,
        bin_wind_direction_end=15,
    )
    expected_wind_direction_range = range(10, 15)
    actual_wind_direction_range = histogram_bin.wind_direction_range
    assert expected_wind_direction_range == actual_wind_direction_range


def test_histogram_bin_measurement_placement():
    histogram_bin = HistogramBin(
        bin_wind_speed_start=0,
        bin_wind_speed_end=5,
        bin_wind_direction_start=10,
        bin_wind_direction_end=15,
    )
    expected_result = True
    actual_result = histogram_bin.can_store_measurement(0, 12)

    assert expected_result == actual_result

