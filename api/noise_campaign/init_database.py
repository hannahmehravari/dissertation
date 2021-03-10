from influxdb import InfluxDBClient
import os


def init_db():
    db_client = InfluxDBClient(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))
    db_client.create_database("observed_data")
    db_client.create_retention_policy("1_hour", "1h", 1, "observed_data", default=True)
    db_client.create_retention_policy("1_week", "7d", 1, "observed_data")
    select_clause = 'SELECT mean("wind_speed") AS "mean_wind_speed", mean("wind_direction") AS "mean_wind_direction"  INTO "1_week"."2min_sample" FROM "30s_sample" GROUP BY time(2m)'
    db_client.create_continuous_query("cq_2m", select_clause, database="observed_data")

    db_client.create_database("predicted_data")
    db_client.create_retention_policy("1_hour", "1h", 1, "predicted_data", default=True)
    db_client.create_database("turbine_status")
    db_client.create_retention_policy("1_week", "7d", 1, "turbine_status", default=True)

    return db_client

