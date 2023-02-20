import argparse
import os

# Default values for arguments
MASTER_HOST = '127.0.0.1'
MASTER_PORT = '5557'
WORKER_COUNT = 16
TEST_TIME = '1h'
USERS = 10000
SPAWN_RATE = 10
LOG_LEVEL = 'INFO'

# Parse command line arguments
parser = argparse.ArgumentParser(description='Start Locust.')
parser.add_argument('profile', type=str, help='Profile to run', choices=['polygon', 'ethereum', 'bsc', 'p', 'e', 'stop'])

parser.add_argument('--workers', type=int, help='Number of workers', default=WORKER_COUNT)
# Update WORKER_COUNT to the value provided in the command line arguments
WORKER_COUNT = parser.parse_args().workers

parser.add_argument('--time', type=str, help='Test time', default=TEST_TIME)
# Update TEST_TIME to the value provided in the command line arguments
TEST_TIME = parser.parse_args().time

parser.add_argument('--users', type=int, help='Number of users', default=USERS)
# Update USERS to the value provided in the command line arguments
USERS = parser.parse_args().users

parser.add_argument('--spawn', type=int, help='Spawn rate', default=SPAWN_RATE)
# Update SPAWN_RATE to the value provided in the command line arguments
SPAWN_RATE = parser.parse_args().spawn

parser.add_argument('--log', type=str, help='Log level', default=LOG_LEVEL)
# Update LOG_LEVEL to the value provided in the command line arguments
LOG_LEVEL = parser.parse_args().log


def start_test(profile: str):
     # If 'p' or 'e' is used as a shorthand for 'polygon' or 'ethereum', convert it to the full name
    if profile == 'p':
        profile = 'polygon'
    elif profile == 'e':
        profile = 'ethereum'
    # Remove any existing test data directory for this profile and create a new one
    if os.path.exists(profile):
        os.system(f"rm -rf {profile}")
    os.system(f"mkdir {profile}")
    # Start the Locust master
    master_command = f"nohup locust --master -f {profile}.py -u {USERS} -r {SPAWN_RATE} " \
                     f"--master-bind-host {MASTER_HOST} --master-bind-port {MASTER_PORT} " \
                     f"-t {TEST_TIME} --html {profile}/report.html --csv {profile}/report.csv " \
                     f" --logfile {profile}/report.log --loglevel {LOG_LEVEL} --expect-workers {WORKER_COUNT} &"
    print(f"Starting master: http://127.0.0.1:8089 {profile}")
    os.system(master_command)
    # Start the Locust workers
    for i in range(WORKER_COUNT):
        os.system(
            f'nohup locust --worker --master-host={MASTER_HOST} --master-port={MASTER_PORT}  -f {profile}.py '
            f'--logfile {profile}/worker_{i}.log &'
        )
        print(f"Starting worker {i + 1} for {profile}")
        # Print out the URL to access the test
    print(f"Run test: http://127.0.0.1:8089 {profile}")


if __name__ == '__main__':
    args = parser.parse_args()
     # Check if the user provided the "stop" argument to stop the running test
    if args.profile == "stop":
        # Kill the current test process
        os.system("pkill -f 'locust.*--master -f'")
    else:
        # Kill any existing Locust processes and start the new test
        try:
            os.system("pkill -f 'locust.*--master -f'")
            print("Previous process was killed")
        except:
            print("Previous testing process wasn`t found")
        start_test(args.profile)
