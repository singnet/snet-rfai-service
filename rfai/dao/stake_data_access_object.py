class StakeDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_stake_details_for_given_request_id(self, request_id):
        query_response = self.repo.execute(
            "SELECT stake_member, stake_amount, claim_back_amount, row_created FROM rfai_stake WHERE request_id = %s",
            [int(request_id)])
        return query_response

    def get_stake_count_for_given_request(self, request_id):
        query_response = self.repo.execute(
            "SELECT COUNT(*) as stake_count FROM rfai_stake WHERE request_id = %s", int(request_id))
        return query_response[0]
