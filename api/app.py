import os
from flask import Flask, jsonify, request
from influxdb import InfluxDBClient
import json
from noise_campaign.measured_state import MeasuredState

app = Flask(__name__)
db_client = InfluxDBClient(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))


@app.route("/turbineStatus", methods=["POST"])
def welcome():

    measured_state = MeasuredState(request.json)

    return jsonify(
        {
            "wind speed": measured_state.average_wind_speed,
            "wind direction": measured_state.average_wind_direction,
            "timestamp": measured_state.timestamp,
        }
    )


if __name__ == "__main__":
    # define the localhost ip and the port that is going to be used
    # in some future article, we are going to use an env variable instead a hardcoded port
    app.run(host="0.0.0.0", port=os.getenv("API_PORT"))

"""
{
  ""turbines"":
    [
      {
        ""id"": ""Garreg Lywd.WTG01"",
        ""requiredRunState"": ""Started"",
        ""timestampUTC"": ""2018-10-16T12:01:00Z""
      },
      {
        ""id"": ""Garreg Lywd.WTG03"",
        ""requiredRunState"": ""Paused"",
        ""timestampUTC"": ""2018-10-16T12:01:35Z""
      },
      {
        ""id"": ""Garreg Lywd.WTG04"",
        ""requiredRunState"": ""Unknown"",
        ""timestampUTC"": ""2018-10-16T12:01:35Z""
      }
    ]
}
"""
