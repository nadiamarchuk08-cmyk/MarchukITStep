import logging
from datetime import datetime

logging.basicConfig(level=logging.INFO,filename="logging.log",filemode="a",format="%(asctime)s - %(levelname)s - %(message)s")

current_date = datetime.now().strftime("%d-%m-%Y")
logging.info(f"Today is: {current_date}")