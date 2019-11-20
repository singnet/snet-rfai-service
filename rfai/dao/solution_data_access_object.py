from rfai.dao.rfai_request_repository import generate_sub_query_for_update_parameters


class SolutionDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_solution_details_for_given_request_id(self, request_id):
        query_response = self.repo.execute(
            "SELECT row_id as rfai_solution_id, submitter, doc_uri, claim_amount, created_at FROM rfai_solution WHERE "
            "request_id = %s", [int(request_id)])
        return query_response

    def get_solution_count_for_given_request(self, request_id):
        query_response = self.repo.execute(
            "SELECT COUNT(*) as solution_count FROM rfai_solution WHERE request_id = %s", int(request_id))
        return query_response[0]

    def add_solution(self, request_id, submitter, doc_uri, claim_amount, created_at):

        query_response = self.repo.execute(
            "INSERT INTO rfai_solution (request_id, submitter, doc_uri, claim_amount, created_at, row_created, "
            "row_updated) "
            "VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
            [request_id, submitter, doc_uri, claim_amount, created_at])

        return query_response[0]

    def update_solution_for_given_request_id(self, request_id, update_parameters):
        sub_query, sub_query_values = generate_sub_query_for_update_parameters(update_parameters=update_parameters)
        query_response = self.repo.execute("UPDATE rfai_solution SET " + update_parameters + " WHERE request_id = %s",
                                           sub_query_values + [request_id])
        return query_response[0]

    def delete_solution_for_given_request_id(self, request_id):
        query_response = self.repo.execute("DELETE FROM rfai_solution WHERE request_id = %s", request_id)
        return query_response[0]
