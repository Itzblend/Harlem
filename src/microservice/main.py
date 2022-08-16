import json
import logging
import os
from logging import config
from time import sleep
from datetime import datetime, timedelta
import random
import requests
import sys
# This sys.path.append is in place so we can import modules from src
sys.path.append(os.path.abspath('../..'))
from src.paths import LOGGING_FILE_PATH

with open(LOGGING_FILE_PATH, 'r') as f:
    logging_config = json.load(f)
logging.config.dictConfig(logging_config)

API_HOST = 'api' if os.getenv('HOSTNAME') == 'microservice' else '127.0.0.1'

def main():
    while True:
        task_creation_time = datetime.now()
        TASK_ALLOCATION_HOURS = random.choice([2, 4, 6, 8, 10])
        task_deadline = task_creation_time + timedelta(hours=TASK_ALLOCATION_HOURS)
        task_name = random.choice(["California", "New York", "Texas", "Florida"])
        severity = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        task_data = \
            {
                "task_creation_time": str(task_creation_time),
                "task_deadline": str(task_deadline),
                "task_allocation_hours": TASK_ALLOCATION_HOURS,
                "task_name": task_name,
                "severity": severity
            }

        resp = requests.post(url=f'http://{API_HOST}:9999/conveyor', data=json.dumps(task_data))
        status = resp.status_code
        if status == 200:
            logging.info("Status OK")
        else:
            logging.error("Error occured while sending task to API")
        sleep(2)

if __name__ == '__main__':
    main()
