import os
from flask import Flask, jsonify, request
import json
from noise_campaign.measured_state import MeasuredState
from noise_campaign.data_handler import DataHandler
from noise_campaign.init_database import init_db

app = Flask(__name__)
db_client = init_db()

@app.route("/turbineStatus", methods=["POST"])
def get_turbine_status():

    measured_state = MeasuredState(request.json)
    data_handler = DataHandler(db_client)

    data_handler.write_measured_state(measured_state)

    return jsonify(
        {
            "wind speed": measured_state.average_wind_speed,
            "wind direction": measured_state.average_wind_direction,
            "timestamp": measured_state.timestamp,
        }
    )


if __name__ == "__main__":
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
