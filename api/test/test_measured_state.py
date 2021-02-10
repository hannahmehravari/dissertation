from datetime import datetime
from noise_campaign.measured_state import MeasuredState
data_dict = {
  "turbines":
    [
      {
        "id": "Garreg Lywd.WTG01",
        "measuredRunState": "Started",
        "averagedWindSpeed": 10.3,
        "averagedWindDirection": 183.0,
        "averagedRotorRPM": 6.1,
        "timestampUTC": "2018-10-16T12:01:00Z"
      },
      {
        "id": "Garreg Lywd.WTG03",
        "measuredRunState": "Paused",
        "averagedWindSpeed": 12.3,
        "averagedWindDirection": 193.0,
        "averagedRotorRPM": 0.0,
        "timestampUTC": "2018-10-16T12:01:35Z"
      }
    ]
}

def test_measured_state_wind_speed():
    measured_state = MeasuredState(data_dict)

    expected_mean_wind_speed = 11.3
    actual_mean_wind_speed = measured_state.average_wind_speed

    assert actual_mean_wind_speed == expected_mean_wind_speed

def test_measured_state_wind_direction():
    measured_state = MeasuredState(data_dict)

    expected_mean_wind_direction = 188.0
    actual_mean_wind_direction = measured_state.average_wind_direction

    assert actual_mean_wind_direction == expected_mean_wind_direction

def test_measured_state_timestamp():
    measured_state = MeasuredState(data_dict)

    expected_timestamp = datetime.strptime('2018-10-16T12:01:00Z', '%Y-%m-%dT%H:%M:%S%z')
    actual_timestamp = measured_state.timestamp

    assert expected_timestamp == actual_timestamp
