def generate_part_query_for_filter_params(filter_parameter):
    if filter_parameter is not None and filter_parameter != {}:
        part_query = "= %s AND ".join(filter_parameter.keys()) + "= %s "
        part_query_values = list(filter_parameter.values())
    else:
        part_query = ""
        part_query_values = list()
    return part_query, part_query_values


class RequestDAO:
    def __init__(self, repo):
        self.repo = repo


    def get_event(self):
        result= self.repo.execute("select * from rfai_events_raw")

        return result


    def get_request_data_for_given_requester_and_status(self, filter_parameter):
        part_query, part_query_values = generate_part_query_for_filter_params(filter_parameter=filter_parameter)
        if part_query != "":
            part_query = " WHERE " + part_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request " + part_query, part_query_values)
        return query_response

    def get_request_status_summary(self):
        query_response = self.repo.execute(
            "SELECT request_id, status, expiration, end_submission, end_evaluation FROM service_request")
        return query_response

    def get_approved_active_request(self, current_block_no, filter_parameter):
        part_query, part_query_values = generate_part_query_for_filter_params(filter_parameter=filter_parameter)
        if part_query != "":
            part_query = " AND " + part_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request WHERE end_submission >= %s" + part_query,
            [current_block_no] + part_query_values)
        return query_response

    def get_approved_solution_vote_request(self, current_block_no, filter_parameter):
        part_query, part_query_values = generate_part_query_for_filter_params(filter_parameter=filter_parameter)
        if part_query != "":
            part_query = " AND " + part_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request "
            "WHERE end_submission < %s AND end_evaluation >= %s" + part_query,
            [current_block_no, current_block_no] + part_query_values)
        return query_response

    def get_approved_completed_request(self, current_block_no, filter_parameter):
        part_query, part_query_values = generate_part_query_for_filter_params(filter_parameter=filter_parameter)
        if part_query != "":
            part_query = " AND " + part_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request  WHERE end_evaluation < %s AND"
            " expiration >= %s" + part_query, [current_block_no, current_block_no] + part_query_values)
        return query_response

    def get_approved_expired_request(self, current_block_no, filter_parameter):
        part_query, part_query_values = generate_part_query_for_filter_params(filter_parameter=filter_parameter)
        if part_query != "":
            part_query = " AND " + part_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request  WHERE expiration < %s" + part_query,
            [current_block_no] + part_query_values)
        return query_response

    def get_open_active_request(self, current_block_no, filter_parameter):
        part_query, part_query_values = generate_part_query_for_filter_params(filter_parameter=filter_parameter)
        if part_query != "":
            part_query = " AND " + part_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request WHERE expiration <= %s" + part_query,
            [current_block_no] + part_query_values)
        return query_response

    def get_open_expired_request(self, current_block_no, filter_parameter):
        part_query, part_query_values = generate_part_query_for_filter_params(filter_parameter=filter_parameter)
        if part_query != "":
            part_query = " AND " + part_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request WHERE expiration > %s " + part_query,
            [current_block_no] + part_query_values)
        return query_response
