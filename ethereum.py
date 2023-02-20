from locust_base import EthRequestConfig, EthereumUser, get_task
from requests_data import ETHRequests


class BSCProfile(EthereumUser):

    eth_requests = [
        EthRequestConfig(
            name="get_transaction_receipt",
            data=ETHRequests.get_transaction_receipt("0x6164b19210d910519a49d14a8ede4168d930429a1867ee10a94264181bc298e1"),
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
            "eth_call", ETHRequests.eth_call("0x0000000000a39bb272e79075ade125fd351887ac"),
            weight=29,
            turn_on=True
        )
    ]
    tasks = [get_task(request) for request in eth_requests if request.turn_on]
