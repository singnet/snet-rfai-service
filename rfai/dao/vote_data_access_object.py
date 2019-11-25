from rfai.dao.rfai_request_repository import generate_sub_query_for_update_parameters
from datetime import datetime as dt


class VoteDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_vote_details_for_given_request_id(self, request_id):
        query_response = self.repo.execute(
            "SELECT rfai_solution_id, COUNT(*) as vote_count FROM rfai_vote WHERE request_id = %s GROUP BY "
            "rfai_solution_id", int(request_id))
        return query_response

    def get_votes_count_for_given_request(self, request_id):
        query_response = self.repo.execute(
            "SELECT COUNT(*) as vote_count FROM rfai_vote WHERE request_id = %s", int(request_id))
        return query_response[0]

    def add_vote(self, request_id, voter, rfai_solution_id, created_at):
        query_response = self.repo.execute(
            "INSERT INTO rfai_vote (request_id, voter, rfai_solution_id, created_at, "
            "row_created, row_updated) "
            "VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
            [request_id, voter, rfai_solution_id, created_at])

        return query_response[0]

    def update_vote_for_given_request_id(self, request_id, update_parameters):
        sub_query, sub_query_values = generate_sub_query_for_update_parameters(update_parameters=update_parameters)
        query_response = self.repo.execute("UPDATE rfai_vote SET " + update_parameters + " WHERE request_id = %s",
                                           sub_query_values + [request_id])
        return query_response[0]

    def delete_vote_for_given_request_id(self, request_id):
        query_response = self.repo.execute("DELETE FROM rfai_vote WHERE request_id = %s", request_id)
        return query_response[0]

    def create_or_update_vote(self, request_id, voter, rfai_solution_id, created_at):
        query_response = self.repo.execute(
            "INSERT INTO rfai_vote (request_id, voter, rfai_solution_id, created_at, "
            "row_created, row_updated) VALUES (%s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP) ON DUPLICATE KEY "
            "UPDATE request_id = %s, voter = %s, rfai_solution_id = %s, row_updated = %s",
            [request_id, voter, rfai_solution_id, created_at, dt.utcnow(), dt.utcnow(), request_id, voter,
             rfai_solution_id, dt.utcnow()])
        return query_response[0]
