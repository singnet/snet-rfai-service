class SolutionDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_solution_details_for_given_request_id(self, request_id):
        query_response = self.repo.execute(
            "SELECT row_id as rfai_solution_id, submitter, doc_uri, claim_amount FROM rfai_solution WHERE request_id = %s",
            [int(request_id)])
        return query_response

    def get_solution_count_for_given_request(self, request_id):
        query_response = self.repo.execute(
            "SELECT COUNT(*) as solution_count FROM rfai_solution WHERE request_id = %s", int(request_id))
        return query_response[0]
