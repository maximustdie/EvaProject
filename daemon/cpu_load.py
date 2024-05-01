import argparse
import logging
import requests

import psutil
from requests.exceptions import InvalidSchema

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default="http://127.0.0.1")
parser.add_argument('--port', type=int, default=8001)

args = parser.parse_args()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = f"{args.host}:{args.port}/cpu/load"
HEADERS = {
    'Content-Type': 'application/json'
}


def send_cpu_load(cpu_load: float):
    try:
        response = requests.post(url=URL, headers=HEADERS, data={"load": cpu_load})
        return response
    except InvalidSchema:
        logging.error(f"Error sending request for {URL}")


def run():
    while True:
        cpu_load = psutil.cpu_percent(interval=10)
        send_cpu_load(cpu_load)
        logging.info(f"cpu load: {cpu_load}%")


if __name__ == "__main__":
    run()
