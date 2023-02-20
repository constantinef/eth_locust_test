class ETHRequests:
    
    # Base JSON-RPC data for all requests
    base_data = {"id": 1, "jsonrpc": "2.0"}

    # Method for getting the latest block
    @classmethod
    def get_latest_block(cls):
        return {"method": "eth_getBlockByNumber", "params": ["latest", True], **cls.base_data}

     # Method for getting a block by its number
    @classmethod
    def get_block_by_number(cls, block_number: str):
        return {"method": "eth_getBlockByNumber", "params": [block_number, True], **cls.base_data}

    # Method for getting a transaction receipt by its hash
    @classmethod
    def get_transaction_receipt(cls, tx_hash: str):
        return {"method": "eth_getTransactionReceipt", "params": [tx_hash], **cls.base_data}

    # Method for getting the balance of an address
    @classmethod
    def get_balance(cls, address: str):
        return {"method": "eth_getBalance", "params": [address, "latest"], **cls.base_data}

    # Method for making an eth_call to an address
    @classmethod
    def eth_call(cls, address: str):
        return {"method": "eth_call", "params": [{"to": address}, "latest"], **cls.base_data}

    # Method for getting the number of transactions sent from an address
    @classmethod
    def eth_get_transaction_count(cls, address: str):
        return {"method": "eth_getTransactionCount", "params": [address, "latest"], **cls.base_data}

    # Method for sending a raw transaction
    @classmethod
    def eth_send_raw_transaction(cls, raw_tx: str):
        return {"method": "eth_sendRawTransaction", "params": [raw_tx], **cls.base_data}

    # Method for getting a transaction by its hash
    @classmethod
    def eth_get_transaction_by_hash(cls, tx_hash: str):
        return {"method": "eth_getTransactionByHash", "params": [tx_hash], **cls.base_data}
