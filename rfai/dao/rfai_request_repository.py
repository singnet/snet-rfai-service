from rfai.dao.common_repository import CommonRepository
from datetime import datetime as dt


def generate_sub_query_for_filter_params(filter_parameter):
    if filter_parameter is not None and filter_parameter != {}:
        sub_query = "= %s AND ".join(filter_parameter.keys()) + "= %s "
        sub_query_values = list(filter_parameter.values())
    else:
        sub_query = ""
        sub_query_values = list()
    return sub_query, sub_query_values


def generate_sub_query_for_update_parameters(update_parameters):
    update_parameters.update({"row_updated": dt.utcnow()})
    if update_parameters is not None and update_parameters != {}:
        sub_query = "= %s , ".join(update_parameters.keys()) + "= %s "
        sub_query_values = list(update_parameters.values())
    else:
        sub_query = ""
        sub_query_values = list()
    return sub_query, sub_query_values


class RFAIRequestRepository(CommonRepository):

    def __init__(self, repo):
        super().__init__(repo)
        self.repo = repo

    def get_claims_data_for_solution_provider(self, submitter, current_block_no):
        query_response = self.repo.execute(
            "SELECT row_id, request_id FROM rfai_solution rs WHERE submitter = %s AND request_id in (SELECT request_id "
            "FROM service_request sr WHERE expiration > %s and end_evaluation < %s) AND row_id IN (SELECT "
            "rfai_solution_id FROM rfai_vote rv)", [submitter, current_block_no, current_block_no])
        return query_response

    def get_vote_details_for_given_request_id(self, request_id):
        query_response = self.repo.execute("SELECT rv.voter, rv.created_at, rs.submitter FROM rfai_vote rv , "
                                           "rfai_solution rs WHERE rv.rfai_solution_id=rs.row_id AND rv.request_id = "
                                           "rs.request_id and rs.request_id = %s ", [request_id])
        return query_response
