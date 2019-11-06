class FoundationMemberDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_foundation_members(self):
        query_response = self.repo.execute(
            "SELECT member_id, member_address, status, row_created FROM foundation_member")
        return query_response
