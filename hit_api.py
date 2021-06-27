import requests
import datetime
import json
import time
import pandas as pd

url = "http://localhost:5000/turbineStatus"

scada_data = pd.read_csv("single_turbine_varda.csv", delimiter=',')

scada_data['timestamp'] =  pd.to_datetime(scada_data['timestamp'], format='%Y-%m-%d %H:%M:%S')

status = "Started"
for index, row in scada_data.iterrows():

  payload = {
    "turbines":
      [
        {
          "id": "Garreg Lywd.WTG01",
          "measuredRunState": status,
          "averagedWindSpeed": row['wind_speed'],
          "averagedWindDirection":row['wind_direction'],
          "averagedRotorRPM": 6.1,
          "timestampUTC": row['timestamp'].strftime('%Y-%m-%dT%H:%M:%SZ')
        }
      ]
  }

  headers = {"Content-Type": "application/json"}

  response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

  print(response.text)

  status = response.json()['turbines'][0]['requiredRunState']

  # time.sleep(0.5)
