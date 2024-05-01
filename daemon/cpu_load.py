import argparse
import logging
import signal
import sys

import requests

import psutil
from requests.exceptions import InvalidSchema, RequestException

parser = argparse.ArgumentParser()
parser.add_argument('--host', type=str, default="http://127.0.0.1")
parser.add_argument('--port', type=int, default=8001)
parser.add_argument('--interval', type=int, default=10)

args = parser.parse_args()

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

URL = f"{args.host}:{args.port}/cpu/load"
HEADERS = {
    'Content-Type': 'application/json'
}


def send_cpu_load(cpu_load: float):
    try:
        response = requests.post(url=URL, headers=HEADERS, json={"load": cpu_load})
        response.raise_for_status()
        return response
    except RequestException as err:
        logging.error(f"Error sending request for {URL}. Detail: {err}")


def run():
    while True:
        cpu_load = psutil.cpu_percent(interval=args.interval)
        logging.info(f"cpu load: {cpu_load}%")

        send_cpu_load(cpu_load)


def signal_handler(signum, frame):
    logging.info("Process terminating...")
    sys.exit(0)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)
    run()
