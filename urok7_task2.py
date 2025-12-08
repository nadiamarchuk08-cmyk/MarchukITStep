import logging

logging.basicConfig(level=logging.ERROR, filename="logg.log", filemode="a", format="%(asctime)s - %(levelname)s - %(message)s")
try:
    x = 1 / 0
except ZeroDivisionError as error:
    logging.error(f"Error: {error}")