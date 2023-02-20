# Requirements
This code requires Locust

```bash
pip install locust
```

# Running the Test
Run the following command to start the test:

```bash
python3 start_test.py {profile_name}
```
This command will use the profile with the same name `{profile}.py` and will collect the results in the directory with `{profile}` name. 
If you run the script again, the results will be recreated - ⚠️ you will lose privious data.

You can set the number of workers, users, and the spawn rate in the start_test.py file.

To specify a specific method to test, modify the eth_requests list in the corresponding profile file, such as bsc.py. For example:

```python
from locust_base import EthRequestConfig, EthereumUser, get_task
from requests_data import ETHRequests


class BSCProfile(EthereumUser):

    eth_requests = [
        EthRequestConfig(
            name="get_transaction_receipt",
            data=ETHRequests.get_transaction_receipt("0x123456"),
            weight=1,
            turn_on=False
        ),
        EthRequestConfig(
            name="get_latest_block",
            data=ETHRequests.get_latest_block(),
            weight=1,
            turn_on=True
        ),
        EthRequestConfig(
            name="get_balance",
            data=ETHRequests.get_balance("0x388c818ca8b9251b393131c08a736a67ccb19297"),
            weight=1,
            turn_on=False
        ),
        EthRequestConfig(
            "eth_call", ETHRequests.eth_call("0x68b3465833fb72A70ecDF485E0e4C7bD8665Fc45"),
            weight=1,
            turn_on=False
        )
    ]
    tasks = [get_task(request) for request in eth_requests if request.turn_on]

```

# Configuring the Test
To customize the test, you can modify the following parameters in the `start_test.py` file:
- worker: The number of workers to run the test.
- user: The number of users to simulate during the test.
- spawn-rate: The spawn rate for users during the test.

# Results
Results of the test will be collected in the `{profile}` directory. 
The test results can be analyzed using the Locust web interface or other visualization tools.
