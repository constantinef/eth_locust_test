from locust_base import EthRequestConfig, EthereumUser, get_task
from requests_data import ETHRequests


class BSCProfile(EthereumUser):

    eth_requests = [
        EthRequestConfig(
            name="get_transaction_receipt",
            data=ETHRequests.get_transaction_receipt("0x4f75868f512c95dc6311d1aad721d7aba88a7be549de39e39f8bd65dbb3b0c4f"),
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
            "eth_call", ETHRequests.eth_call("0xfa500178de024bf43cfa69b7e636a28ab68f2741"),
            weight=29,
            turn_on=True
        )
    ]
    tasks = [get_task(request) for request in eth_requests if request.turn_on]
