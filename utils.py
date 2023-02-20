import json
import logging
import sys
import time
from json import JSONDecodeError

from locust.clients import LocustResponse
from locust.exception import RescheduleTask

logger = logging.getLogger(__name__)

# This function checks for specific HTTP status codes and logs the message accordingly.
def check_for_fatal_errors(response: LocustResponse):
    logger.info(f"{response.status_code} {response.url} {response.text}")
    if response.status_code == 401:
        logger.error("⛔️ Unauthorized request to %s", response.url)
    elif response.status_code == 404:
        logger.error("⛔️ Not found request to %s", response.url)
    elif response.status_code >= 500 and response.status_code <= 599:
        logger.error("⛔️ Internal server error %s", response.url)
    elif response.status_code >= 300 and response.status_code <= 399:
        logger.error("⛔️ Redirect error %s", response.url)

# This function checks if the response from an HTTP request is valid.
def check_response(response):
    if response.status_code != 200:
        logger.info("Response has an incorrect status code: %s", response.status_code)
        logger.info("Response content: %s", response.text)
        check_for_fatal_errors(response)
        response.failure(f"Response has an incorrect status code: {response.status_code}")
        response.raise_for_status()
    try:
        response_json = response.json()
    except JSONDecodeError as err:
        logger.info("Got JSONDecodeError during decoding a response: %s", err)
        logger.info("Got JSONDecodeError during decoding a response: %s", response.content)
        response.failure("JSONDecodeError during decoding a response")
        raise RescheduleTask() from err

    if "jsonrpc" not in response_json:
        logger.info("Response is not a JSON-RPC: %s", json.dumps(response_json))
        response.failure("Response is not a JSON-RPC")
        raise RescheduleTask()

    if "error" in response_json:
        logger.info("Response has a JSON-RPC error: %s", json.dumps(response_json))
        if "code" in response_json["error"]:
            response.failure(f"Response has a JSON-RPC error {response_json['error']['code']}")
            raise RescheduleTask()
        response.failure("Response has a JSON-RPC error without a specific code")
        raise RescheduleTask()
    
    if not response_json.get("result"):
        logger.info("Response hasn't a result: %s", json.dumps(response_json))

# This class creates timers to measure the duration of specific events during the test.
class Timer:
    _timer: dict = {}

    @classmethod
    def set_timer(cls, timer_id):
        cls._timer[timer_id] = time.time()

    @classmethod
    def get_time_diff(cls, timer_id):
        return time.time() - cls._timer[timer_id]
