from common.logger import get_logger
import os
from common.blockchain_util import BlockChainUtil
from common.ipfs_util import IPFSUtil
from rfai.config import NETWORK
from rfai.consumers.event_consumer import EventConsumer
from rfai.dao.foundation_member_data_access_object import FoundationMemberDAO
from rfai.dao.request_data_access_object import RequestDAO
import datetime
from common.repository import Repository
from rfai.dao.stake_data_access_object import StakeDAO
from rfai.rfai_status import RFAIStatusCodes

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

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        requester = event_data['requester']
        expiration = event_data['expiration']
        amount = event_data['amount']
        metadata_hash = self._get_metadata_hash(event_data['documentURI'])

        self._process_create_request_event(request_id, requester, expiration, amount, metadata_hash)

    def _process_create_request_event(self, request_id, requester, expiration, amount, metadata_hash):
        [found, requestId, requester, totalFund, documentURI, expiration, endSubmission, endEvaluation, status,
         stakeMembers, submitters] = self._get_rfai_service_request_by_id(request_id)
        rfai_metadata = eval(self._get_rfai_metadata_from_ipfs(metadata_hash))

        title = rfai_metadata['title']
        requestor_name = requester
        description = rfai_metadata['description']
        git_hub_link = ''
        training_data_set_uri = rfai_metadata['training-dataset']
        acceptance_criteria = rfai_metadata['acceptance-criteria']
        request_actor = ''
        created_at = rfai_metadata['created']

        self._rfai_request_repository.create_request(request_id, requester, totalFund, metadata_hash, expiration,
                                                     endSubmission, endEvaluation, status, title, requestor_name,
                                                     description, git_hub_link, training_data_set_uri,
                                                     acceptance_criteria, request_actor, created_at)


class RFAIExtendRequestEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, ws_provider, ipfs_url, ipfs_port):
        super().__init__(ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        # need to change this whenever we clean up it should nto be tied with db column name
        event_data = self._get_event_data(event)

        expiration = event_data['expiration']
        requester = event_data['requester']
        request_id = event_data['requestId']

        filter_params = {"expiration": expiration}
        self._rfai_request_repository.update_request_for_given_request_id(request_id, filter_params)


class RFAIApproveRequestEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        # need to change this whenever we clean up it should nto be tied with db column name
        event_data = self._get_event_data(event)

        request_id = event_data['requestId']
        approver = event_data['approver']
        endSubmission = event_data['endSubmission']
        endEvaluation = event_data['endEvaluation']
        expiration = event_data['expiration']

        filter_params = {"status": RFAIStatusCodes.APPROVED.value, "request_actor": approver,
                         "end_submission": endSubmission, "end_evaluation": endEvaluation, "expiration": expiration}
        self._rfai_request_repository.update_request_for_given_request_id(request_id, filter_params)

        # from where we will get claim back amount


class RFAIFundRequestEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)
    _stake_dao_repository = StakeDAO(_connection)

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)

        request_id = event_data['requestId']
        staker = event_data['staker']
        amount = event_data['amount']
        [found, request_id, requester, total_fund, document_uri, expiration, end_submission, end_evaluation, status,
         stake_members, submitters] = self._get_rfai_service_request_by_id(request_id)

        metadata_hash = self._get_metadata_hash(document_uri)
        rfai_metadata = eval(self._get_rfai_metadata_from_ipfs(metadata_hash))
        created_at = rfai_metadata['created']

        # from where we will get claim back amount

        self._stake_dao_repository.create_stake(request_id, staker, amount, 0, created_at)


class RFAIAddFoundationMemberEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_foundation_member_repository = FoundationMemberDAO(_connection)

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        member = event_data['member']
        actor = event_data['actor']
        role = event_data['role']
        status = event_data['status']
        # check for last attribute caretaed_at rigtn ow set as current time . aslo this should be upsert query
        self._rfai_foundation_member_repository.add_foundation_member(role, member, status, actor,
                                                                      datetime.datetime.utcnow())


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


class RFAIRejectRequestEventConsumer(RFAIEventConsumer):
    _connection = Repository(NETWORKS=NETWORK)
    _rfai_request_repository = RequestDAO(_connection)

    def __init__(self, net_id, ws_provider, ipfs_url, ipfs_port):
        super().__init__(net_id, ws_provider, ipfs_url, ipfs_port)

    def on_event(self, event):
        event_data = self._get_event_data(event)
        request_id = event_data['requestId']
        [found, request_id, requester, total_fund, document_uri, expiration, end_submission, end_evaluation, status,
         stake_members, submitters] = self._get_rfai_service_request_by_id(request_id)
        self._update_rfai_request_status_and_actor(request_id=request_id, status=RFAIStatusCodes.REJECTED.value,
                                                   request_actor=event_data["actor"])

    def _update_rfai_request_status_and_actor(self, request_id, status, request_actor):
        self._rfai_request_repository.update_request_for_given_request_id(request_id=request_id, update_parameters={
            "status": status, "request_actor": request_actor})
