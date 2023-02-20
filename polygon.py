from locust_base import EthRequestConfig, EthereumUser, get_task
from requests_data import ETHRequests


class BSCProfile(EthereumUser):

    eth_requests = [
        EthRequestConfig(
            name="get_transaction_receipt",
            data=ETHRequests.get_transaction_receipt("0x2e8ff2bb85210ffd8650b63979aa8bd28464845c7f650b8192f8e9bc71f878ae"),
            weight=22,
            turn_on=True
        ),
        EthRequestConfig(
            name="get_block_by_number",
            data=ETHRequests.get_block_by_number("latest"),
            weight=16,
            turn_on=True
        ),
        EthRequestConfig(
            name="get_block_by_number",
            data=ETHRequests.get_block_by_number("earliest"),
            weight=16,
            turn_on=True
        ),
        EthRequestConfig(
            name="get_block_by_number",
            data=ETHRequests.get_block_by_number("pending"),
            weight=16,
            turn_on=True
        ),
        EthRequestConfig(
            "eth_call", ETHRequests.eth_call("0x31f3f75b7c44f6bf0b9b86291152e21fdf68b293"),
            weight=29,
            turn_on=True
        )
    ]
    tasks = [get_task(request) for request in eth_requests if request.turn_on]
