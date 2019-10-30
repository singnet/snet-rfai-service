from rfai.dao.request_data_access_object import RequestDAO
from rfai.rfai_status import RFAIStatus

class RFAIService:
    def __init__(self, repo):
        self.request_dao = RequestDAO(repo=repo)

    def get_requests(self, status, requester):
        if status.upper() in RFAIStatus.__members__:
            request_status = RFAIStatus[status.upper()].value
        else:
            raise Exception("Invalid Request status.")
        return self.request_dao.get_request_data_for_given_requester_and_status(status=request_status, requester=requester)
