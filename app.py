from logger import logging

def add(a,b):
    logging.debug(f"Adding {a} and {b}")
    return a+b

logging.debug("Starting the application")
add(5,10)