import json
from noise_campaign.smartstop_measurement_names import SMARTStopMeasurementNames
from noise_campaign.histogram import Histogram
from statistics import mean
from datetime import datetime
import pytz

class MeasuredState:
    def __init__(self, histogram: Histogram, request_json: dict):
        data_dict = request_json
        self.average_wind_speed = self._extract_average_measurement(data_dict, SMARTStopMeasurementNames.wind_speed)
        self.average_wind_direction = self._extract_average_measurement(data_dict, SMARTStopMeasurementNames.wind_direction)

        self.wind_speed_bin = histogram.get_wind_speed_bin(self.average_wind_speed)
        self.wind_direction_bin = histogram.get_wind_direction_bin(self.average_wind_direction)

        self.status = data_dict['turbines'][0]['measuredRunState']

        self.timestamp = self._get_time_stamp(data_dict)

    def _get_time_stamp(self, data_dict):
        d = datetime.strptime(data_dict['turbines'][0]['timestampUTC'], "%Y-%m-%dT%H:%M:%SZ")
        d.replace(tzinfo=pytz.UTC)
        return d

    def _extract_average_measurement(self, data_dict, measurement):
        turbines = data_dict['turbines']
        measurement_list = []
        for turbine in turbines:
            measurement_list.append(turbine[measurement])
        return mean(measurement_list)


        

