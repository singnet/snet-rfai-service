from rfai.dao.request_data_access_object import RequestDAO
from rfai.dao.vote_data_access_object import VoteDAO
from rfai.dao.solution_data_access_object import SolutionDAO
from rfai.dao.stake_data_access_object import StakeDAO
from rfai.rfai_status import RFAIStatus


class RFAIService:
    def __init__(self, repo):
        self.request_dao = RequestDAO(repo=repo)
        self.vote_dao = VoteDAO(repo=repo)
        self.solution_dao = SolutionDAO(repo=repo)
        self.stake_dao = StakeDAO(repo=repo)

    def get_requests(self, status, requester):
        if status.upper() in RFAIStatus.__members__:
            request_status = RFAIStatus[status.upper()].value
        else:
            raise Exception("Invalid request status.")
        return self.request_dao.get_request_data_for_given_requester_and_status(status=request_status,
                                                                                requester=requester)

    def get_rfai_summary(self):
        return {}

    def get_vote_details_for_given_request_id(self, request_id):
        vote_data = self.vote_dao.get_vote_details_for_given_request_id(request_id=request_id)
        return vote_data

    def get_stake_details_for_given_request_id(self, request_id):
        stake_data = self.stake_dao.get_stake_details_for_given_request_id(request_id=request_id)
        return stake_data

    def get_solution_details_for_given_request_id(self, request_id):
        solution_data = self.solution_dao.get_solution_details_for_given_request_id(request_id=request_id)
        return solution_data
