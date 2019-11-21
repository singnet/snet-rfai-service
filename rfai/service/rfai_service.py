from common.blockchain_util import BlockChainUtil
from common.utils import Utils
from rfai.config import NETWORK
from rfai.dao.foundation_member_data_access_object import FoundationMemberDAO
from rfai.dao.request_data_access_object import RequestDAO
from rfai.dao.solution_data_access_object import SolutionDAO
from rfai.dao.stake_data_access_object import StakeDAO
from rfai.dao.vote_data_access_object import VoteDAO
from rfai.rfai_status import RFAIStatusCodes

obj_utils = Utils()
obj_blockchain_utils = BlockChainUtil(provider_type="HTTP_PROVIDER", provider=NETWORK["http_provider"])


class RFAIService:
    def __init__(self, repo):
        self.request_dao = RequestDAO(repo=repo)
        self.vote_dao = VoteDAO(repo=repo)
        self.solution_dao = SolutionDAO(repo=repo)
        self.stake_dao = StakeDAO(repo=repo)
        self.foundation_member_dao = FoundationMemberDAO(repo=repo)

    def _format_filter_params(self, query_parameters):
        filter_params = {}
        # if "status" in query_parameters.keys():
        #     filter_params["status"] = RFAIStatusCodes.query_parameters["status"].value
        if "requester" in query_parameters.keys():
            filter_params["requester"] = query_parameters["requester"]
        if "request_id" in query_parameters.keys():
            filter_params["request_id"] = query_parameters["request_id"]
        return filter_params

    def get_requests(self, query_string_parameters):
        status = query_string_parameters.get("status", None)
        filter_parameter = self._format_filter_params(query_parameters=query_string_parameters)
        if status is not None and status.upper() in RFAIStatusCodes.__members__:
            status_code = RFAIStatusCodes[status.upper()].value
            query_string_parameters["status_code"] = status_code
            current_block_no = obj_blockchain_utils.get_current_block_no()

            if status_code == RFAIStatusCodes.ACTIVE.value:
                requests_data = self.request_dao.get_approved_active_request(current_block_no=current_block_no,
                                                                             filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.SOLUTION_VOTE.value:
                requests_data = self.request_dao.get_approved_solution_vote_request(current_block_no=current_block_no,
                                                                                    filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.COMPLETED.value:
                requests_data = self.request_dao.get_approved_completed_request(current_block_no=current_block_no,
                                                                                filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.PENDING.value:
                requests_data = self.request_dao.get_open_active_request(current_block_no=current_block_no,
                                                                         requester=query_string_parameters[
                                                                             "requester"],
                                                                         filter_parameter=filter_parameter)

            elif status_code == RFAIStatusCodes.INCOMPLETE.value:
                requests_data = self.request_dao.get_open_expired_request(current_block_no=current_block_no,
                                                                          filter_parameter=filter_parameter)

            else:
                requests_data = self.request_dao.get_request_data_for_given_requester_and_status(
                    filter_parameter=filter_parameter)
        elif status is None:
            requests_data = self.request_dao.get_request_data_for_given_requester_and_status(
                filter_parameter=filter_parameter)

        for record in requests_data:
            vote_count = self.vote_dao.get_votes_count_for_given_request(request_id=record["request_id"])
            stake_count = self.stake_dao.get_stake_count_for_given_request(request_id=record["request_id"])
            solution_count = self.solution_dao.get_solution_count_for_given_request(request_id=record["request_id"])
            record.update({"vote_count": vote_count["vote_count"]})
            record.update({"stake_count": stake_count["stake_count"]})
            record.update({"solution_count": solution_count["solution_count"]})
            record["created_at"] = str(record["created_at"])
        return requests_data

    def get_rfai_summary(self, requester, my_request):
        request_summary = self.generate_rfai_summary(requester=requester, my_request=my_request)
        # request_summary_raw = self.request_dao.get_request_status_summary()
        # request_summary = {RFAIStatusCodes(0).name: {"count": 0}, RFAIStatusCodes(1).name: {"count": 0},
        #                    RFAIStatusCodes(2).name: {"count": 0}, RFAIStatusCodes(4).name: {"count": 0}}
        # for record in request_summary_raw:
        #     status_code = int(record["status"])
        #     status = RFAIStatusCodes(status_code).name
        #     if status_code == RFAIStatusCodes.OPEN.value or status_code == RFAIStatusCodes.APPROVED.value:
        #         vote_data = self.vote_dao.get_vote_details_for_given_request_id(request_id=record["request_id"])
        #         has_vote = True if len(vote_data) > 0 else False
        #         sub_status = self.compute_rfai_request_sub_status(status=status,
        #                                                           end_submission=int(record["end_submission"]),
        #                                                           end_evaluation=int(record["end_evaluation"]),
        #                                                           expiration=int(record["expiration"]),
        #                                                           has_vote=has_vote)
        #         request_summary[status][sub_status] = request_summary[status].get(sub_status, 0) + 1
        #     request_summary[status]["count"] = request_summary[status]["count"] + 1

        return request_summary

    def get_vote_details_for_given_request_id(self, request_id):
        vote_data = self.vote_dao.get_vote_details_for_given_request_id(request_id=request_id)
        return vote_data

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

    # def compute_rfai_request_sub_status(self, status, end_submission, end_evaluation, expiration, has_vote=False):
    #     current_block_no = obj_blockchain_utils.get_current_block_no()
    #     if status == RFAIStatusCodes(0).name:
    #         if current_block_no > expiration:
    #             return RFAIStatus.OPEN.value.EXPIRED.value
    #         else:
    #             return RFAIStatus.OPEN.value.ACTIVE.value
    #     elif status == RFAIStatusCodes(1).name:
    #         if current_block_no <= end_submission:
    #             return RFAIStatus.APPROVED.value.ACTIVE.value
    #         elif end_submission <= current_block_no <= end_evaluation:
    #             return RFAIStatus.APPROVED.value.SOLUTION_VOTE.value
    #         elif end_evaluation <= current_block_no <= expiration:
    #             return RFAIStatus.APPROVED.value.COMPLETED.value
    #         elif current_block_no >= expiration and has_vote:
    #             return RFAIStatus.APPROVED.value.COMPLETED.value
    #         elif current_block_no >= expiration:
    #             return RFAIStatus.APPROVED.value.EXPIRED.value
    #     raise Exception("Unable to compute RFAI request sub status")

    def generate_rfai_summary(self, requester, my_request):
        filter_parameter = {}
        current_block_no = obj_blockchain_utils.get_current_block_no()
        rfai_summary = {
            "PENDING": len(self.request_dao.get_open_active_request(current_block_no=current_block_no,
                                                                    requester=requester,
                                                                    filter_parameter=filter_parameter)),
            "INCOMPLETE": len(self.request_dao.get_open_expired_request(current_block_no=current_block_no,
                                                                        filter_parameter=filter_parameter))
                          + len(self.request_dao.get_approved_expired_request(current_block_no=current_block_no,
                                                                              filter_parameter=filter_parameter)),
            "ACTIVE": len(self.request_dao.get_approved_active_request(current_block_no=current_block_no,
                                                                       filter_parameter=filter_parameter)),
            "SOLUTION_VOTE": len(self.request_dao.get_approved_solution_vote_request(
                current_block_no=current_block_no,
                filter_parameter=filter_parameter)),
            "COMPLETED": len(self.request_dao.get_approved_completed_request(current_block_no=current_block_no,
                                                                             filter_parameter=filter_parameter)),
            "REJECTED": len(self.request_dao.get_request_data_for_given_requester_and_status(
                filter_parameter={"status": RFAIStatusCodes.REJECTED.value})),
            "CLOSED": len(self.request_dao.get_request_data_for_given_requester_and_status(
                filter_parameter={"status": RFAIStatusCodes.CLOSED.value}))
        }
        return rfai_summary
