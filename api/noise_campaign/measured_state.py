import json
from noise_campaign.smartstop_measurement_names import SMARTStopMeasurementNames
from statistics import mean
from datetime import datetime
class MeasuredState:
    def __init__(self, request_json: dict):
        data_dict = request_json
        self.average_wind_speed = self._extract_average_measurement(data_dict, SMARTStopMeasurementNames.wind_speed)
        self.average_wind_direction = self._extract_average_measurement(data_dict, SMARTStopMeasurementNames.wind_direction)
        self.timestamp = self._get_time_stamp(data_dict)

    def _get_time_stamp(self, data_dict):
        timestamp_string = data_dict['turbines'][0]['timestampUTC']
        timestamp_datetime = datetime.strptime(timestamp_string, '%Y-%m-%dT%H:%M:%S%z')
        return timestamp_datetime

    def _extract_average_measurement(self, data_dict, measurement):
        turbines = data_dict['turbines']
        measurement_list = []
        for turbine in turbines:
            measurement_list.append(turbine[measurement])
        return mean(measurement_list)

        

