import json
import logging
import os
from logging import config
from time import sleep
import sys
# This sys.path.append is in place so we can import modules from src
sys.path.append(os.path.abspath('../..'))
from src.paths import LOGGING_FILE_PATH

with open(LOGGING_FILE_PATH, 'r') as f:
    logging_config = json.load(f)
logging.config.dictConfig(logging_config)

def main():
    while True:
        logging.info('Logging action')
        sleep(5)

if __name__ == '__main__':
    main()
