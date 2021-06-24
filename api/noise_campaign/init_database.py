from influxdb import InfluxDBClient, DataFrameClient
import os


def init_db():
    db_client = DataFrameClient(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))

    db_client.create_database("30s_observed_data")
    db_client.create_retention_policy("2_weeks", "14d", 1, "30s_observed_data", default=True)

    db_client.create_database("10min_observed_data")
    db_client.create_retention_policy("2_weeks", "14d", 1, "10min_observed_data", default=True)

    db_client.create_database("predicted_data")
    db_client.create_retention_policy("2_weeks", "14d", 1, "predicted_data", default=True)


    return db_client

