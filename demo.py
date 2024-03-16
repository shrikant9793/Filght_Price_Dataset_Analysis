from flight_price_dataset.logger import logging
from flight_price_dataset.exception import flight_price_Exception
import sys


#logging.info("Welcome to custome logging")

try:
    a = 1 / "10"
    #logging.info("Welcome to custome logging")
except Exception as e:
    logging.info(e)
    raise  flight_price_Exception(e, sys) from e

