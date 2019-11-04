class StakeDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_stake_details_for_given_request_id(self, request_id):
        query_response = self.repo.execute(
            "SELECT stake_member, stake_amount, claim_back_amount FROM rfai_stake WHERE request_id = %s",
            [int(request_id)])
        return query_response
