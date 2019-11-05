class RequestDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_request_data_for_given_requester_and_status(self, requester, status):
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor FROM service_request WHERE requester = %s AND status = %s",
            [requester, status])
        return query_response

    def get_request_status_summary(self):
        query_response = self.repo.execute("SELECT status, count(*) as request_count FROM service_request GROUP BY status")
        return query_response
