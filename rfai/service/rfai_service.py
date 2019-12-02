from common.blockchain_util import BlockChainUtil
from common.utils import Utils
from rfai.config import NETWORK
from rfai.dao.foundation_member_data_access_object import FoundationMemberDAO
from rfai.dao.request_data_access_object import RequestDAO
from rfai.dao.solution_data_access_object import SolutionDAO
from rfai.dao.stake_data_access_object import StakeDAO
from rfai.dao.vote_data_access_object import VoteDAO
from rfai.dao.rfai_request_repository import RFAIRequestRepository
from rfai.rfai_status import RFAIStatusCodes
import json
from common.logger import get_logger

obj_utils = Utils()
obj_blockchain_utils = BlockChainUtil(provider_type="HTTP_PROVIDER", provider=NETWORK["http_provider"])
logger = get_logger(__name__)


class RFAIService:
    def __init__(self, repo):
        self.request_dao = RequestDAO(repo=repo)
        self.vote_dao = VoteDAO(repo=repo)
        self.solution_dao = SolutionDAO(repo=repo)
        self.stake_dao = StakeDAO(repo=repo)
        self.foundation_member_dao = FoundationMemberDAO(repo=repo)
        self.rfai_request_dao = RFAIRequestRepository(repo=repo)

    def _format_filter_params(self, query_parameters):
        filter_params = {}
        # if "requester" in query_parameters.keys():
        #     filter_params["requester"] = query_parameters["requester"]
        if "request_id" in query_parameters.keys():
            filter_params["request_id"] = query_parameters["request_id"]
        return filter_params

    def get_requests(self, query_string_parameters):
        status = query_string_parameters.get("status", None)
        status = status.upper()
        filter_parameter = self._format_filter_params(query_parameters=query_string_parameters)
        if status is not None and status in RFAIStatusCodes.__members__:
            status_code = RFAIStatusCodes[status].value
            query_string_parameters["status_code"] = status_code
            current_block_no = obj_blockchain_utils.get_current_block_no()

            if status_code == RFAIStatusCodes.ACTIVE.value:
                tmp_requests_data = self.request_dao.get_approved_active_request(current_block_no=current_block_no,
                                                                                 filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.SOLUTION_VOTE.value:
                tmp_requests_data = self.request_dao.get_approved_solution_vote_request(
                    current_block_no=current_block_no,
                    filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.COMPLETED.value:
                tmp_requests_data = self.request_dao.get_approved_completed_request(current_block_no=current_block_no,
                                                                                    filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.PENDING.value:
                tmp_requests_data = self.request_dao.get_open_active_request(current_block_no=current_block_no,
                                                                             requester=query_string_parameters[
                                                                                 "requester"],
                                                                             filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.CLOSED.value:
                tmp_requests_data = self.request_dao.get_closed_request(requester=query_string_parameters["requester"],
                                                                        filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.INCOMPLETE.value:
                tmp_requests_data = self.request_dao.get_open_expired_request(current_block_no=current_block_no,
                                                                              filter_parameter=filter_parameter) + \
                                    self.request_dao.get_approved_expired_request(current_block_no=current_block_no,
                                                                                  filter_parameter=filter_parameter) + \
                                    self.request_dao.get_approved_request_with_no_votes(
                                        current_block_no=current_block_no,
                                        filter_parameter=filter_parameter)
            else:
                filter_parameter.update({"status": getattr(RFAIStatusCodes, status).value})
                tmp_requests_data = self.request_dao.get_request_data_for_given_requester_and_status(
                    filter_parameter=filter_parameter)
        elif status is None:
            tmp_requests_data = self.request_dao.get_request_data_for_given_requester_and_status(
                filter_parameter=filter_parameter)

        my_request = query_string_parameters.get("my_request", "false")
        requests = []
        for record in tmp_requests_data:
            if my_request.lower() == "true" and query_string_parameters["requester"] != record["requester"]:
                continue
            vote_count = self.vote_dao.get_votes_count_for_given_request(request_id=record["request_id"])
            stake_count = self.stake_dao.get_stake_count_for_given_request(request_id=record["request_id"])
            solution_count = self.solution_dao.get_solution_count_for_given_request(request_id=record["request_id"])
            record.update({"vote_count": vote_count["vote_count"]})
            record.update({"stake_count": stake_count["stake_count"]})
            record.update({"solution_count": solution_count["solution_count"]})
            record["created_at"] = str(record["created_at"])
            requests.append(record)
        logger.info(requests)
        return requests

    def get_rfai_summary(self, requester, my_request):
        request_summary = self.generate_rfai_summary(requester=requester, my_request=my_request)
        return request_summary

    def get_vote_details_for_given_request_id(self, request_id):
        vote_details = self.rfai_request_dao.get_vote_details_for_given_request_id(request_id=request_id)
        for record in vote_details:
            record["created_at"] = str(record["created_at"])
        return vote_details

    def get_stake_details_for_given_request_id(self, request_id):
        stake_data = self.stake_dao.get_stake_details_for_given_request_id(request_id=request_id)
        for record in stake_data:
            record["created_at"] = str(record["created_at"])
        return stake_data

    def get_solution_details_for_given_request_id(self, request_id):
        solution_data = self.solution_dao.get_solution_details_for_given_request_id(request_id=request_id)
        for record in solution_data:
            record["created_at"] = str(record["created_at"])
        return solution_data

    def get_foundation_members(self):
        foundation_members_data = self.foundation_member_dao.get_foundation_members()
        for record in foundation_members_data:
            record["status"] = obj_utils.bits_to_integer(record["status"])
            record["role"] = obj_utils.bits_to_integer(record["role"])
            record["created_at"] = str(record["created_at"])
        return foundation_members_data

    def generate_rfai_summary(self, requester, my_request):
        filter_parameter = {}
        current_block_no = obj_blockchain_utils.get_current_block_no()
        rfai_summary = {
            "PENDING": len(self.get_requests(query_string_parameters={"requester": requester,
                                                                      "status": RFAIStatusCodes.PENDING.name,
                                                                      "my_request": my_request})),
            "INCOMPLETE": len(self.get_requests(query_string_parameters={"requester": requester,
                                                                         "status": RFAIStatusCodes.INCOMPLETE.name,
                                                                         "my_request": my_request})),
            "ACTIVE": len(self.get_requests(query_string_parameters={"requester": requester,
                                                                     "status": RFAIStatusCodes.ACTIVE.name,
                                                                     "my_request": my_request})),
            "SOLUTION_VOTE": len(self.get_requests(query_string_parameters={"requester": requester,
                                                                            "status": RFAIStatusCodes.SOLUTION_VOTE.name,
                                                                            "my_request": my_request})),
            "COMPLETED": len(self.get_requests(query_string_parameters={"requester": requester,
                                                                        "status": RFAIStatusCodes.COMPLETED.name,
                                                                        "my_request": my_request})),
            "REJECTED": len(self.get_requests(query_string_parameters={"requester": requester,
                                                                       "status": RFAIStatusCodes.REJECTED.name,
                                                                       "my_request": my_request})),
            "CLOSED": len(self.get_requests(query_string_parameters={"requester": requester,
                                                                     "status": RFAIStatusCodes.CLOSED.name,
                                                                     "my_request": my_request}))
        }
        return rfai_summary

    def get_claims_data_for_solution_provider(self, user_address):
        current_block_no = obj_blockchain_utils.get_current_block_no()
        solution_data = self.rfai_request_dao.get_claims_data_for_solution_provider(submitter=user_address,
                                                                                    current_block_no=current_block_no)
        for record in solution_data:
            request_id = record["request_id"]
            request_data = self.request_dao.get_request_data_for_given_requester_and_status(
                filter_parameter={"request_id": request_id})
            votes = self.vote_dao.get_vote_details_for_given_rfai_solution_id(rfai_solution_id=record["row_id"])
            claim_amount_data = self.rfai_request_dao.get_claim_amount_for_solution_provider(
                rfai_solution_id=record["row_id"])
            record.update({"request_title": request_data[0]["request_title"], "votes": votes["votes"],
                           "expiration": request_data[0]["expiration"],
                           "tokens": int(claim_amount_data[0]["claim_amount_for_soln_provider"]),
                           "end_evaluation": request_data[0]["end_evaluation"]})
        return solution_data

    def get_claims_data_for_stake_provider(self, user_address):
        current_block_no = obj_blockchain_utils.get_current_block_no()
        stake_data = self.rfai_request_dao.get_claim_details_for_stakers(stake_member=user_address,
                                                                         current_block_no=current_block_no)
        for record in stake_data:
            record["status"] = RFAIStatusCodes(record["status"]).name
            record["claim_back_amount"] = self.stake_dao.get_stake_details_for_given_request_id_and_stake_member(
                request_id=record["request_id"], stake_member=user_address)[0]["claim_back_amount"]
        return stake_data
