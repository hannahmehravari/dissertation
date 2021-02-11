import requests
import datetime
import json

url = "http://localhost:5000/turbineStatus"

now = datetime.datetime.now()
date_time = now.strftime('%Y-%m-%dT%H:%M:%S%z')

payload = {
  "turbines":
    [
      {
        "id": "Garreg Lywd.WTG01",
        "measuredRunState": "Started",
        "averagedWindSpeed": 12.3,
        "averagedWindDirection": 150.0,
        "averagedRotorRPM": 6.1,
        "timestampUTC": date_time
      }
    ]
}

headers = {"Content-Type": "application/json"}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)
