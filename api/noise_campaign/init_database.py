from influxdb import InfluxDBClient, DataFrameClient
import os


def init_db():
    db_client = DataFrameClient(host=os.getenv("DB_HOST"), port=os.getenv("DB_PORT"))

    try:
        db_client.query("DROP DATABASE \"noise_campaign\"")
    except:
        pass

    db_client.create_database("noise_campaign")
    # db_client.create_retention_policy("2_weeks", "14d", 1, "noise_campaign", default=True)

    return db_client

