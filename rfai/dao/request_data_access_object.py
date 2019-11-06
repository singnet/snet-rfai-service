class RequestDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_request_data_for_given_requester_and_status(self, filter_parameter):
        part_query = "= %s AND ".join(filter_parameter.keys()) + "= %s "
        part_query_values = list(filter_parameter.values())
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor FROM service_request WHERE " + part_query,
            part_query_values)
        return query_response

    def get_request_status_summary(self):
        query_response = self.repo.execute(
            "SELECT request_id, status, expiration, end_submission, end_evaluation FROM service_request")
        return query_response
