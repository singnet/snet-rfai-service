from common.blockchain_util import BlockChainUtil
from common.utils import Utils
from rfai.config import NETWORK
from rfai.dao.foundation_member_data_access_object import FoundationMemberDAO
from rfai.dao.request_data_access_object import RequestDAO
from rfai.dao.solution_data_access_object import SolutionDAO
from rfai.dao.stake_data_access_object import StakeDAO
from rfai.dao.vote_data_access_object import VoteDAO
from rfai.rfai_status import RFAIStatusCodes, RFAIStatus

obj_utils = Utils()
obj_blockchain_utils = BlockChainUtil(provider_type="HTTP_PROVIDER", provider=NETWORK["http_provider"])


class RFAIService:
    def __init__(self, repo):
        self.request_dao = RequestDAO(repo=repo)
        self.vote_dao = VoteDAO(repo=repo)
        self.solution_dao = SolutionDAO(repo=repo)
        self.stake_dao = StakeDAO(repo=repo)
        self.foundation_member_dao = FoundationMemberDAO(repo=repo)

    def validate_request_filter_parameters(self, params):
        for param in params:
            if param in ['requester', 'status', 'request_id']:
                pass
            else:
                raise Exception("Bad query parameters.")

    def get_requests(self, query_string_parameters):
        status = query_string_parameters.get("status", None)
        self.validate_request_filter_parameters(params=query_string_parameters.keys())
        if status is not None and status.upper() in RFAIStatusCodes.__members__:
            query_string_parameters["status"] = RFAIStatusCodes[status.upper()].value
        else:
            raise Exception("Invalid request status.")
        requests_data = self.request_dao.get_request_data_for_given_requester_and_status(
            filter_parameter=query_string_parameters)
        for record in requests_data:
            vote_count = self.vote_dao.get_votes_count_for_given_request(request_id=record["request_id"])
            stake_count = self.stake_dao.get_stake_count_for_given_request(request_id=record["request_id"])
            solution_count = self.solution_dao.get_solution_count_for_given_request(request_id=record["request_id"])
            record.update({"vote_count": vote_count["vote_count"]})
            record.update({"stake_count": stake_count["stake_count"]})
            record.update({"solution_count": solution_count["solution_count"]})
        return requests_data

    def get_rfai_summary(self):
        request_summary_raw = self.request_dao.get_request_status_summary()
        request_summary = {RFAIStatusCodes(0).name: {"count": 0}, RFAIStatusCodes(1).name: {"count": 0},
                           RFAIStatusCodes(2).name: {"count": 0}, RFAIStatusCodes(4).name: {"count": 0}}
        for record in request_summary_raw:
            status_code = int(record["status"])
            status = RFAIStatusCodes(status_code).name
            if status_code == RFAIStatusCodes.OPEN.value or status_code == RFAIStatusCodes.APPROVED.value:
                vote_data = self.vote_dao.get_vote_details_for_given_request_id(request_id=record["request_id"])
                has_vote = True if len(vote_data) > 0 else False
                sub_status = self.compute_rfai_request_sub_status(status=status,
                                                                  end_submission=int(record["end_submission"]),
                                                                  end_evaluation=int(record["end_evaluation"]),
                                                                  expiration=int(record["expiration"]),
                                                                  has_vote=has_vote)
                request_summary[status][sub_status] = request_summary[status].get(sub_status, 0) + 1
            request_summary[status]["count"] = request_summary[status]["count"] + 1

        return request_summary

    def get_vote_details_for_given_request_id(self, request_id):
        vote_data = self.vote_dao.get_vote_details_for_given_request_id(request_id=request_id)
        return vote_data

    def get_stake_details_for_given_request_id(self, request_id):
        stake_data = self.stake_dao.get_stake_details_for_given_request_id(request_id=request_id)
        return stake_data

    def get_solution_details_for_given_request_id(self, request_id):
        solution_data = self.solution_dao.get_solution_details_for_given_request_id(request_id=request_id)
        return solution_data

    def get_foundation_members(self):
        foundation_members_data = self.foundation_member_dao.get_foundation_members()
        for record in foundation_members_data:
            record["status"] = obj_utils.bits_to_integer(record["status"])
        return foundation_members_data

    def compute_rfai_request_sub_status(self, status, end_submission, end_evaluation, expiration, has_vote=False):
        current_block_no = obj_blockchain_utils.get_current_block_no()
        if status == RFAIStatusCodes(0).name:
            if current_block_no > expiration:
                return RFAIStatus.OPEN.value.EXPIRED.value
            else:
                return RFAIStatus.OPEN.value.ACTIVE.value
        elif status == RFAIStatusCodes(1).name:
            if current_block_no <= end_submission:
                return RFAIStatus.APPROVED.value.ACTIVE.value
            elif current_block_no >= end_submission and current_block_no <= end_evaluation:
                return RFAIStatus.APPROVED.value.SOLUTION_VOTE.value
            elif current_block_no >= end_evaluation and current_block_no <= expiration:
                return RFAIStatus.APPROVED.value.COMPLETED.value
            elif current_block_no >= expiration and has_vote:
                return RFAIStatus.APPROVED.value.COMPLETED.value
            elif current_block_no >= expiration:
                return RFAIStatus.APPROVED.value.EXPIRED.value
        raise Exception("Unable to compute RFAI request sub status")
