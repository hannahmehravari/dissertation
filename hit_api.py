import requests
import datetime
import json
import time
import pandas as pd

url = "http://localhost:5000/turbineStatus"
scada_data = pd.read_csv("C:\\Users\\hanna\\Desktop\\data\\Events.csv", delimiter=',',  parse_dates=True)
scada_data.drop(columns=['timestamp ($ts)_DateTime','payload_quality_String', 'payload_timestamp_DateTime', 'payload_unit_String', 'payload_quantity_String'], inplace=True)

scada_data.rename(columns={'timestamp  (UTC+00:00) Local - Europe/London: GMT_DateTime':'timestamp',
                          'apiKey_String': 'turbine', 'measurement_String': 'measurement', 'payload_value_Double' : 'value'}, inplace=True)
scada_data['timestamp'] = pd.to_datetime(scada_data['timestamp'])

wind_speed = scada_data[scada_data['measurement'] == 'Windspeed'][["timestamp","turbine","value"]]
wind_speed.rename(columns={"value": "wind_speed"}, inplace=True)
wind_speed.reset_index(inplace=True, drop=True)
wind_direction = scada_data[scada_data['measurement'] == 'WindDirection'][["timestamp","turbine","value"]]
wind_direction.rename(columns={"value": "wind_direction"}, inplace=True)
wind_direction.reset_index(inplace=True, drop=True)
wind_speed['wind_direction'] = wind_direction['wind_direction']
data = wind_speed.copy()

turbine = data['turbine'].unique()[0]

data_filtered = data[data['turbine'] == turbine]

data_filtered.to_csv('single_turbine_varda.csv')

# status = "Started"
# for index, row in data_filtered.iterrows():
#   now = datetime.datetime.now()
#   date_time = now.strftime('%Y-%m-%dT%H:%M:%SZ')

#   payload = {
#     "turbines":
#       [
#         {
#           "id": "Garreg Lywd.WTG01",
#           "measuredRunState": status,
#           "averagedWindSpeed": row['wind_speed'],
#           "averagedWindDirection":row['wind_direction'],
#           "averagedRotorRPM": 6.1,
#           "timestampUTC": date_time
#         }
#       ]
#   }

#   headers = {"Content-Type": "application/json"}

#   response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

#   print(response.text)

#   status = response.json()['state']

#   time.sleep(5)
