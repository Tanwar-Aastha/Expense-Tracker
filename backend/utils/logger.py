import logging
import os
from datetime import datetime


# Defining the log directories name
LOG_FILE_NAME = f"{datetime.now().strftime("%d_%m_%Y_%H_%M_%S")}"

# Joining the log file name with the cirrent working directory
LOG_DIR_PATH = os.path.join(os.getcwd(), "logs", LOG_FILE_NAME)

# Creating directories for every log
os.makedirs(name=LOG_DIR_PATH, exist_ok=True)

LOG_FILE_PATH = os.path.join(LOG_DIR_PATH, LOG_FILE_NAME)


# Setting up basic configurations of logging message
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)