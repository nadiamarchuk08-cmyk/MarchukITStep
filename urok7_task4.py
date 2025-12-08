import logging

logging.basicConfig(level=logging.INFO,filename="a.log",filemode="a",format="%(asctime)s - %(levelname)s - %(message)s")

def check_age(age):
    try:
        assert age >= 18
        logging.info("You can use this service")
    except AssertionError:
        logging.error("You must be 18+ years old")

input_age = int(input("Enter your age: "))
check_age(input_age)