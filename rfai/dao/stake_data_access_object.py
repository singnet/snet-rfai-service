from rfai.dao.request_data_access_object import generate_sub_query_for_update_parameters


class StakeDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_stake_details_for_given_request_id(self, request_id):
        query_response = self.repo.execute(
            "SELECT stake_member, stake_amount, claim_back_amount, created_at FROM rfai_stake WHERE request_id = %s",
            [int(request_id)])
        return query_response

    def get_stake_count_for_given_request(self, request_id):
        query_response = self.repo.execute(
            "SELECT COUNT(*) as stake_count FROM rfai_stake WHERE request_id = %s", int(request_id))
        return query_response[0]

    def create_stake(self, request_id, stake_member, stake_amount, claim_back_amount, created_at):

        query_response = self.repo.execute(
            "INSERT INTO rfai_stake (request_id, stake_member, stake_amount, claim_back_amount, created_at, "
            "row_created, row_updated) "
            "VALUES (%s, %s, %s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
            [request_id, stake_member, stake_amount, claim_back_amount, created_at])

        return query_response[0]

    def update_stake_for_given_request_id(self, request_id, update_parameters):
        sub_query, sub_query_values = generate_sub_query_for_update_parameters(update_parameters=update_parameters)
        query_response = self.repo.execute("UPDATE rfai_stake SET " + update_parameters + " WHERE request_id = %s",
                                           sub_query_values + [request_id])
        return query_response[0]

    def delete_stake_for_given_request_id(self, request_id):
        query_response = self.repo.execute("DELETE FROM rfai_stake WHERE request_id = %s", request_id)
        return query_response[0]
