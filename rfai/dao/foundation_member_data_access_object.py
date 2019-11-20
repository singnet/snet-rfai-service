from rfai.dao.rfai_request_repository import generate_sub_query_for_update_parameters


class FoundationMemberDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_foundation_members(self):
        query_response = self.repo.execute(
            "SELECT member_id, member_address, status, created_at FROM foundation_member")
        return query_response

    def add_foundation_member(self, member_id, member_address, status, request_actor, created_at):
        query_response = self.repo.execute(
            "INSERT INTO foundation_member (member_id, member_address, status, request_actor, created_at, row_created, "
            "row_updated) "
            "VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
            [member_id, member_address, status, request_actor, created_at])

        return query_response[0]

    def update_foundation_member_for_given_member_id(self, member_id, update_parameters):
        sub_query, sub_query_values = generate_sub_query_for_update_parameters(update_parameters=update_parameters)
        query_response = self.repo.execute(
            "UPDATE foundation_member SET " + update_parameters + " WHERE member_id = %s", sub_query_values +
            [member_id])
        return query_response[0]

    def delete_foundation_member_for_given_member_id(self, member_id):
        query_response = self.repo.execute("DELETE FROM foundation_member WHERE member_id = %s", member_id)
        return query_response[0]