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
    
    # Method for getting the gas price
    @classmethod
    def eth_gas_price(cls):
        return {"method": "eth_gasPrice", **cls.base_data}
    
    # Method for eth_getLogs
    @classmethod
    def eth_get_logs(cls, from_block: str, to_block: str, address: str):
        return {"method": "eth_getLogs", "params": [{"fromBlock": from_block, "toBlock": to_block, "address": address}], **cls.base_data}
    
    # Method for eth_chainId
    @classmethod
    def eth_chain_id(cls):
        return {"method": "eth_chainId", **cls.base_data}
    
    # Method for eth_estimateGas
    @classmethod
    def eth_estimate_gas(cls, tx: dict):
        return {"method": "eth_estimateGas", "params": [tx], **cls.base_data}
    
    # Method for eth_getBlockTransactionCountByNumber
    @classmethod
    def eth_get_block_transaction_count_by_number(cls, block_number: str):
        return {"method": "eth_getBlockTransactionCountByNumber", "params": [block_number], **cls.base_data}
    
    # Method for eth_getBlockByHash
    @classmethod
    def eth_get_block_by_hash(cls, block_hash: str):
        return {"method": "eth_getBlockByHash", "params": [block_hash, True], **cls.base_data}
    
    # Method for eth_getBlockTransactionCountByHash
    @classmethod
    def eth_get_block_transaction_count_by_hash(cls, block_hash: str):
        return {"method": "eth_getBlockTransactionCountByHash", "params": [block_hash], **cls.base_data}
    
    # Method for eth_getTransactionByBlockHashAndIndex
    @classmethod
    def eth_get_transaction_by_block_hash_and_index(cls, block_hash: str, index: str):
        return {"method": "eth_getTransactionByBlockHashAndIndex", "params": [block_hash, index], **cls.base_data}
    
    # Method for eth_getTransactionByBlockNumberAndIndex
    @classmethod
    def eth_get_transaction_by_block_number_and_index(cls, block_number: str, index: str):
        return {"method": "eth_getTransactionByBlockNumberAndIndex", "params": [block_number, index], **cls.base_data}
    
    # Method for eth_getStorageAt
    @classmethod
    def eth_get_storage_at(cls, address: str, position: str):
        return {"method": "eth_getStorageAt", "params": [address, position, "latest"], **cls.base_data}
    
    # Method for eth_getCode
    @classmethod
    def eth_get_code(cls, address: str):
        return {"method": "eth_getCode", "params": [address, "latest"], **cls.base_data}
    
    # Method for debug_getBadBlocks
    @classmethod
    def debug_get_bad_blocks(cls):
        return {"method": "debug_getBadBlocks", **cls.base_data}
    
    # Method for debug_getStoragerangeAt
    @classmethod
    def debug_get_storage_range_at(cls, block_hash: str, tx_index: str, address: str, position: str, max_result: str):
        return {"method": "debug_getStorageRangeAt", "params": [block_hash, tx_index, address, position, max_result], **cls.base_data}
    
    # Method for debug_traceBlock
    @classmethod
    def debug_trace_block(cls, block_number: str):
        return {"method": "debug_traceBlock", "params": [block_number], **cls.base_data}
    
    # Method for debug_traceBlockByNumber
    @classmethod
    def debug_trace_block_by_number(cls, block_number: str):
        return {"method": "debug_traceBlockByNumber", "params": [block_number], **cls.base_data}
    
    # Method for debug_traceBlockByHash
    @classmethod
    def debug_trace_block_by_hash(cls, block_hash: str):
        return {"method": "debug_traceBlockByHash", "params": [block_hash], **cls.base_data}
    
    # Method for debug_tracecall
    @classmethod
    def debug_trace_call(cls, tx: dict):
        return {"method": "debug_traceCall", "params": [tx], **cls.base_data}
    
    # Method for debug_traceTransaction
    @classmethod
    def debug_trace_transaction(cls, tx_hash: str):
        return {"method": "debug_traceTransaction", "params": [tx_hash], **cls.base_data}
    
    # Method for eth_blockNumber
    @classmethod
    def eth_block_number(cls):
        return {"method": "eth_blockNumber", **cls.base_data}
    
    # Method for eth_getBlockReceipts
    @classmethod
    def eth_get_block_receipts(cls, block_hash: str):
        return {"method": "eth_getBlockReceipts", "params": [block_hash], **cls.base_data}
    
    # Method for eth_getBlockTransactionCountByHash
    @classmethod
    def eth_get_block_transaction_count_by_hash(cls, block_hash: str):
        return {"method": "eth_getBlockTransactionCountByHash", "params": [block_hash], **cls.base_data}
    
    # Method for eth_getBlockTransactionCountByNumber
    @classmethod
    def eth_get_block_transaction_count_by_number(cls, block_number: str):
        return {"method": "eth_getBlockTransactionCountByNumber", "params": [block_number], **cls.base_data}
    
    # Method for eth_getFilterChanges
    @classmethod
    def eth_get_filter_changes(cls, filter_id: str):
        return {"method": "eth_getFilterChanges", "params": [filter_id], **cls.base_data}
    
    # Method for eth_getFilterLogs
    @classmethod
    def eth_get_filter_logs(cls, filter_id: str):
        return {"method": "eth_getFilterLogs", "params": [filter_id], **cls.base_data}
    
    # Method for eth_getTransactionByBlockHashAndIndex
    @classmethod
    def eth_get_transaction_by_block_hash_and_index(cls, block_hash: str, index: str):
        return {"method": "eth_getTransactionByBlockHashAndIndex", "params": [block_hash, index], **cls.base_data}
    
    # Method for eth_getTransactionByBlockNumberAndIndex
    @classmethod
    def eth_get_transaction_by_block_number_and_index(cls, block_number: str, index: str):
        return {"method": "eth_getTransactionByBlockNumberAndIndex", "params": [block_number, index], **cls.base_data}
    
    # Method for eth_mining
    @classmethod
    def eth_mining(cls):
        return {"method": "eth_mining", **cls.base_data}
    
    # Method for eth_newBlockFilter
    @classmethod
    def eth_new_block_filter(cls):
        return {"method": "eth_newBlockFilter", **cls.base_data}
    
    # Method for eth_newFilter
    @classmethod
    def eth_new_filter(cls, filter: dict):
        return {"method": "eth_newFilter", "params": [filter], **cls.base_data}
    
    # Method for eth_newPendingTransactionFilter
    @classmethod
    def eth_new_pending_transaction_filter(cls):
        return {"method": "eth_newPendingTransactionFilter", **cls.base_data}
    
    # Method for eth_signTransaction
    @classmethod
    def eth_sign_transaction(cls, tx: dict):
        return {"method": "eth_signTransaction", "params": [tx], **cls.base_data}
    
    # Method for eth_subscribe
    @classmethod
    def eth_subscribe(cls, subscription_type: str, subscription_params: dict):
        return {"method": "eth_subscribe", "params": [subscription_type, subscription_params], **cls.base_data}
    
    # Method for eth_syncing
    @classmethod
    def eth_syncing(cls):
        return {"method": "eth_syncing", **cls.base_data}
    
    # Method for eth_unsubscribe
    @classmethod
    def eth_unsubscribe(cls, subscription_id: str):
        return {"method": "eth_unsubscribe", "params": [subscription_id], **cls.base_data}
    
    # Method for net_listening
    @classmethod
    def net_listening(cls):
        return {"method": "net_listening", **cls.base_data}
    
    # Method for net_peerCount
    @classmethod
    def net_peer_count(cls):
        return {"method": "net_peerCount", **cls.base_data}
    
    # Method for net_version
    @classmethod
    def net_version(cls):
        return {"method": "net_version", **cls.base_data}
    
    # Method for web3_clientVersion
    @classmethod
    def web3_client_version(cls):
        return {"method": "web3_clientVersion", **cls.base_data}
    
