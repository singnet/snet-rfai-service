class StakeDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_stake_details_for_given_request_id(self, request_id):
        return [request_id]