import logging

logging.basicConfig(level=logging.INFO,filename="auth.log",filemode="a",format="%(asctime)s - %(levelname)s - %(message)s")

def login(username, password):
    correct_username = "admin"
    correct_password = "12345"

    try:
        assert username == correct_username and password == correct_password
        logging.info("Login Successful")
    except AssertionError:
        logging.error("Incorrect username or password")

login("admin", "12345")
login("user", "0000")