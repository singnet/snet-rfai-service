from common.logger import get_logger
from web3 import Web3
import json

import os

from common.blockchain_util import BlockChainUtil
from common.ipfs_util import IPFSUtil
from rfai.consumers.event_consumer import EventConsumer

from rfai.dao.rfai_request_repository import RFAIRequestRepository

from common.repository import Repository
from rfai.config import NETWORK_ID, NETWORK

logger = get_logger(__name__)


class RFAIRequestEventConsumer(EventConsumer):
    _connection = Repository(NETWORK_ID, NETWORKS=NETWORK)
    _rfai_request_repository = RFAIRequestRepository(_connection)

    def __init__(self, ws_provider, ipfs_url, ipfs_port):
        self._ipfs_util = IPFSUtil(ipfs_url, ipfs_port)
        self._blockchain_util = BlockChainUtil("WS_PROVIDER", ws_provider)

    def on_event(self, event):
        pass

    def _get_rfai_contract(self):
        net_id = NETWORK_ID
        base_contract_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', '..', 'node_modules', 'singularitynet-rfai-contracts'))
        registry_contract = self._blockchain_util.get_contract_instance(base_contract_path, "RFAI", net_id)

        return registry_contract

    def _get_request_details_from_blockchain(self, event):
        logger.info(f"processing RFAI request event {event}")
        rfai_contract = self._get_rfai_contract()


class CreateRequestEventConsumer(RFAIRequestEventConsumer):

    def on_event(self, event):
        # request_id, request_blockchain_data, request_ipfs_data, request_document_uri = \
        #     self._get_request_details_from_blockchain(event)

        # self._process_create_request_event(request_id, request_blockchain_data, request_ipfs_data,
        #                                                request_document_uri)
        pass

    def _process_create_request_event(self, request_id, request_blockchain_data, request_ipfs_data,
                                      request_document_uri):

        try:
            pass
        except Exception as e:
            self._rfai_request_repository.rollback_transaction()
            raise e


class ExtendRequestEventConsumer(CreateRequestEventConsumer):
    pass


class ApproveRequestEventConsumer(RFAIRequestEventConsumer):

    def on_event(self, event):
        # request_id, request_blockchain_data, request_ipfs_data, request_document_uri = \
        #     self._get_request_details_from_blockchain(event)
        # self._process_approve_request_event(request_id)
        pass

    def _process_approve_request_event(self, request_id):
        try:
            pass
        except Exception as e:
            logger.exception(str(e))
            self._rfai_request_repository.rollback_transaction()
            raise e
