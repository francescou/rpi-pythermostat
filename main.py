"""
remote thermostat API
"""

import logging
from influxdb import InfluxDBClient
from requests.exceptions import ConnectionError
import serial

DB_NAME = "telegraf"

logging.basicConfig(level=logging.INFO)
logging.getLogger("requests.packages.urllib3.connectionpool").setLevel(logging.WARNING)


CLIENT = InfluxDBClient(host='influx', database=DB_NAME)

CLIENT.ping()
