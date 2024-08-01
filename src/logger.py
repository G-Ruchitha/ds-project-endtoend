'''
This code sets up a logging system in Python.
'''

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

'''
 creates a string with the current date and time formatted as MM_DD_YYYY_HH_MM_SS. 
 This ensures that each log file has a unique name based on the timestamp.
'''
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

'''
 os.getcwd() returns the current working directory. os.path.join is used to concatenate 
 the current working directory, a subdirectory named "logs", and the log file name to 
 form the complete path where the log file will be stored.
'''
os.makedirs(logs_path,exist_ok=True)

'''
os.makedirs creates the directory structure specified by logs_path. 
The exist_ok=True parameter ensures that no error is raised if the directory already exists.
'''
LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

'''
Generates the full file path for the log file.
resulting in the complete path where the log file will be saved.
'''
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

'''
Configures the logging system using logging.basicConfig
Specifies the path to the log file where logs will be written.
Defines the format of the log messages. 
Sets the logging level to INFO. This means that log messages with severity 
INFO and higher (e.g., WARNING, ERROR, CRITICAL) will be recorded. 
Messages with lower severity levels (e.g., DEBUG) will not be recorded.
'''
