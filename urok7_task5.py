import logging

logging.basicConfig(level=logging.INFO,filename="list.log",filemode="a",format="%(asctime)s - %(levelname)s - %(message)s")

def process_list(input_list):
    try:
        assert len(input_list) >= 3
        logging.info(f"list contains {len(input_list)} elements")
    except AssertionError:
        logging.error("list must contain 3 or more elements")


process_list([1, 2, 3])
process_list([0])