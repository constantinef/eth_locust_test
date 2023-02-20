import logging
import sys
from dataclasses import dataclass
from typing import List
from datetime import datetime

from locust import HttpUser, task, between, events
from locust.runners import MasterRunner, WorkerRunner


from utils import check_response, Timer

logger = logging.getLogger(__name__)


@dataclass
class EthRequestConfig:
    name: str
    data: dict
    weight: int = 1
    turn_on: bool = True


# Create a task from the given request configuration
def get_task(request: EthRequestConfig):
    @task(request.weight)
    def return_task(self):
        self.run_request(request)
    return return_task


# Define the base Ethereum user class
class EthereumUser(HttpUser):
    # Set the wait time between requests
    wait_time = between(0, 2)
    eth_requests: List[EthRequestConfig] = []
    abstract = True
    # Create a list of tasks for this user based on the configured requests
    tasks = [get_task(request) for request in eth_requests if request.turn_on]

    # Make a request for the given request configuration
    def run_request(self, request: EthRequestConfig):
        if not request.turn_on:
            return
        with self.client.post(self.host, json=request.data, name=request.name, catch_response=True) as response:
            check_response(response)


# Listener for the test start event
@events.test_start.add_listener
def on_test_start(environment, **_kwargs):
    # It will be called for any runner (master, worker, local)
    if not isinstance(environment.runner, MasterRunner):
        # Print worker details to the log
        logger.debug(
            f"Worker[{environment.runner.worker_index:02d}]: "
            f"The test is started, Environment: {environment.runner}",
        )
        Timer.set_timer(environment.runner.worker_index)
    else:
        # Print master details to the log
        logger.info(
            f"Master: test_start.add_listener: The test is started, "
            f"Environment: {environment.runner}",
        )


# Listener for the test stop event
@events.test_stop.add_listener
def on_test_stop(environment, **_kwargs):
    # It will be called for any runner (master, worker, local)
    runner = environment.runner
    # Save the web UI report
    runner.save_web_ui(f"{str(datetime.now())}_{runner.__class__.__name__}_report.html")
    if not isinstance(runner, MasterRunner):
        # Print worker details to the log
        logger.info(
            f"🏁 Worker[{runner.worker_index:02d}]: Tests completed in "
            f"{Timer.get_time_diff(runner.worker_index):>.3f} seconds"
        )
    else:
        # Print master details to the log
        logger.info("🏁 Master: The test is stopped")


# Listener for the init event
@events.init.add_listener
def on_init(environment, **_kwargs):
    # It will be called for any runner (master, worker, local)
    logger.debug("init.add_listener: Init is started")
    logger.debug("init.add_listener: Environment: %s", environment.runner)
    logger.debug("init.add_listener: Host: %s", environment.host)

    host_under_test = environment.host or "Default host"

    if isinstance(environment.runner, MasterRunner):
        # Print master details to the log
        logger.info("🤖 I'm a master. Running tests for %s", host_under_test)

    if not isinstance(environment.runner, WorkerRunner):
        # Print worker details to the log
        logger.info("🤖 I'm a worker. Running tests for %s", host_under_test)
