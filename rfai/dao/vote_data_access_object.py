class VoteDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_vote_details_for_given_request_id(self, request_id):
        query_response = self.repo.execute(
            "SELECT rfai_solution_id, COUNT(*) as vote_count FROM rfai_vote WHERE request_id = %s GROUP BY rfai_solution_id",
            int(request_id))
        return query_response
