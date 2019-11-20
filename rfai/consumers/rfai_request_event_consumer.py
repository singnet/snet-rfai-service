from common.logger import get_logger
import os
from common.blockchain_util import BlockChainUtil
from common.ipfs_util import IPFSUtil
from rfai.config import NETWORK
from rfai.consumers.event_consumer import EventConsumer
from rfai.dao.request_data_access_object import RequestDAO

from common.repository import Repository

logger = get_logger(__name__)


class RFAIEventConsumer(EventConsumer):

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        self._ipfs_util = IPFSUtil(ipfs_url, ipfs_port)
        self._blockchain_util = BlockChainUtil("WS_PROVIDER", ws_provider)
        self._net_id = net_id

    def on_event(self, event):
        pass

    def _get_rfai_contract(self):
        base_contract_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'node_modules', 'singularitynet-rfai-contracts'))
        rfai_contract = self._blockchain_util.get_contract_instance(base_contract_path, "RFAI", self._net_id)

        return rfai_contract

    def _get_rfai_metadata_from_ipfs(self, ipfs_hash):
        return self._ipfs_util.read_file_from_ipfs(ipfs_hash)

    def _get_event_data(self, event):
        return eval(event['data']['json_str'])

    def _get_metadata_hash(self, metadata_uri):
        return metadata_uri.decode("utf-8")

    def _get_rfai_service_request_by_id(self, request_id):
        rfai_contract = self._get_rfai_contract()
        result = self._blockchain_util.call_contract_function(rfai_contract, "getServiceRequestById", request_id)
        return result


class RFAICreateRequestEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, ws_provider, ipfs_url, ipfs_port):
        super().__init__(ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):

        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        requester = event_data['requester']
        expiration = event_data['expiration']
        amount = event_data['amount']
        metadata_hash = self._get_metadata_hash(event_data['documentURI'])
        rfai_metadata = self._get_rfai_metadata_from_ipfs(metadata_hash)

        self._process_create_request_event(request_id, requester, expiration, amount, rfai_metadata)

    def _process_create_request_event(self, request_id, requester, expiration, amount, rfai_metadata):

        try:
            print(2)
        except Exception as e:

            raise e


class ExtendRequestEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, ws_provider, ipfs_url, ipfs_port):
        super().__init__(ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        result = self._get_rfai_service_request_by_id(request_id)
        print(result)


class ApproveRequestEventConsumer(RFAIEventConsumer):

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


class RFAIFundRequestEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        result = self._get_rfai_service_request_by_id(request_id)
        print(result)


class RFAIAddFoundationMember(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        result = self._get_rfai_service_request_by_id(request_id)
        print(result)


class RFAIAddSolutionRequestEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        result = self._get_rfai_service_request_by_id(request_id)
        print(result)


class RFAIRejectRequestEvent(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        result = self._get_rfai_service_request_by_id(request_id)
        print(result)
