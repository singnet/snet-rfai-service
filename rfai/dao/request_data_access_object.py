from rfai.dao.rfai_request_repository import generate_sub_query_for_update_parameters, \
    generate_sub_query_for_filter_params

from datetime import datetime as dt
from rfai.rfai_status import RFAIStatusCodes


class RequestDAO:
    def __init__(self, repo):
        self.repo = repo

    def get_event(self):
        result = self.repo.execute("select * from rfai_events_raw")

        return result

    def get_request_data_for_given_requester_and_status(self, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " WHERE " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request " + sub_query, sub_query_values)
        return query_response

    def get_request_status_summary(self):
        query_response = self.repo.execute(
            "SELECT request_id, status, expiration, end_submission, end_evaluation FROM service_request")
        return query_response

    def get_approved_active_request(self, current_block_no, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " AND " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request WHERE status = 1 AND "
            "end_submission >= %s" + sub_query,
            [current_block_no] + sub_query_values)
        return query_response

    def get_approved_solution_vote_request(self, current_block_no, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " AND " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request "
            "WHERE status = 1 AND end_submission < %s AND end_evaluation >= %s" + sub_query,
            [current_block_no, current_block_no] + sub_query_values)
        return query_response

    def get_approved_completed_request(self, current_block_no, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " AND " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request  WHERE status = 1 AND "
            "end_evaluation < %s AND request_id IN (SELECT request_id FROM rfai_vote) " + sub_query,
            [current_block_no] + sub_query_values)
        return query_response

    def get_approved_expired_request(self, current_block_no, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " AND " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request  WHERE status = 1 AND (expiration < %s "
            "OR (expiration > %s AND request_id NOT IN (SELECT request_id FROM rfai_vote)))" + sub_query,
            [current_block_no, current_block_no] + sub_query_values)
        return query_response

    def get_open_active_request(self, current_block_no, requester, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " AND " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request WHERE (SELECT count(*) FROM "
            "foundation_member WHERE  member_address = %s or requester = %s) AND status = 0 and expiration >= %s"
            + sub_query, [requester, requester, current_block_no] + sub_query_values)
        return query_response

    def get_open_expired_request(self, current_block_no, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " AND " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request WHERE status = 0 AND expiration < %s "
            + sub_query, [current_block_no] + sub_query_values)
        return query_response

    def get_closed_request(self, requester, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " AND " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request WHERE (SELECT count(*) FROM "
            "foundation_member WHERE  member_address = %s or requester = %s) AND status = 4"
            + sub_query, [requester, requester] + sub_query_values)
        return query_response

    def create_request(self, request_id, requester, fund_total, document_uri, expiration, end_submission,
                       end_evaluation, status, request_title, requester_name, description, git_hub_link,
                       training_data_set_uri, acceptance_criteria, request_actor, created_at):

        query_response = self.repo.execute(
            "INSERT INTO service_request (request_id, requester, fund_total, documentURI,  expiration, end_submission, "
            "end_evaluation, status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria,  request_actor, created_at, row_created, row_updated) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)",
            [request_id, requester, fund_total, document_uri, expiration, end_submission, end_evaluation, status,
             request_title, requester_name, description, git_hub_link, training_data_set_uri, acceptance_criteria,
             request_actor, created_at, dt.utcnow(), dt.utcnow()])

        return query_response[0]

    def update_request_for_given_request_id(self, request_id, update_parameters):
        sub_query, sub_query_values = generate_sub_query_for_update_parameters(update_parameters=update_parameters)
        query_response = self.repo.execute("UPDATE service_request SET " + sub_query + " WHERE request_id = %s",
                                           sub_query_values + [request_id])
        return query_response[0]

    def delete_request_for_given_request_id(self, request_id):
        query_response = self.repo.execute("DELETE FROM service_request WHERE request_id = %s", request_id)
        return query_response[0]

    def get_approved_request_with_no_votes(self, current_block_no, filter_parameter):
        sub_query, sub_query_values = generate_sub_query_for_filter_params(filter_parameter=filter_parameter)
        if sub_query != "":
            sub_query = " AND " + sub_query
        query_response = self.repo.execute(
            "SELECT request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, "
            "status, request_title, requester_name, description, git_hub_link, training_data_set_uri, "
            "acceptance_criteria, request_actor, created_at FROM service_request WHERE expiration > %s AND "
            "end_evaluation < %s AND request_id NOT IN (select request_id FROM rfai_vote rv) " + sub_query,
            [current_block_no, current_block_no] + sub_query_values)
        return query_response
