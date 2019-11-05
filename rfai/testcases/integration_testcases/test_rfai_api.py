import json
import unittest
from unittest.mock import patch

from rfai.requests_for_ai_handler import request_handler, get_vote_for_request_handler, get_stake_for_request_handler, \
    get_solution_for_request_handler, get_foundation_members_handler, rfai_summary_handler


class TestRFAIAPI(unittest.TestCase):
    def setUp(self):
        pass

    # @patch("common.utils.Utils.report_slack")
    # def test_get_request_for_given_requester(self, mock_report_slack):
    #     event = {"resource": "/request", "httpMethod": "GET",
    #              "queryStringParameters": {"requester": "0xf15BB7b899250a67C02fcEDA18706B79aC997884", "status": "Open"}}
    #     response = request_handler(event=event, context=None)
    #     assert (response["statusCode"] == 200)
    #     response_body = json.loads(response["body"])
    #     assert (response_body["status"] == "success")
    #     assert (response_body["data"] == [
    #         {'request_id': 1, 'requester': '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 'fund_total': 100,
    #          'documentURI': '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 'expiration': 123456,
    #          'end_submission': 123457, 'end_evaluation': 123458, 'status': 0, 'request_title': 'Face Recognition',
    #          'requester_name': 'Dummy', 'description': 'Detecting faces from various perspective.',
    #          'git_hub_link': 'http://www.dummy.io/repo',
    #          'training_data_set_uri': '0xg15BB7b899250a67C02fcEDA18706B79aC997884',
    #          'acceptance_criteria': 'This is dummy . All are invited.', 'request_actor': 'Dummy Actor'}])
    #
    # @patch("common.utils.Utils.report_slack")
    # def test_get_vote_for_given_request_id(self, mock_report_slack):
    #     event = {"resource": "/request/1/vote", "httpMethod": "GET",
    #              "pathParameters": {"request_id": 1}}
    #     response = get_vote_for_request_handler(event=event, context=None)
    #     print(response)
    #     assert (response["statusCode"] == 200)
    #     response_body = json.loads(response["body"])
    #     assert (response_body["status"] == "success")
    #     print(response_body)
    #     assert (response_body["data"] == [{'rfai_solution_id': '1', 'vote_count': 1},
    #                                       {'rfai_solution_id': '2', 'vote_count': 1}])
    #
    # @patch("common.utils.Utils.report_slack")
    # def test_get_stake_for_given_request_id(self, mock_report_slack):
    #     event = {"resource": "/request/1/stake", "httpMethod": "GET",
    #              "pathParameters": {"request_id": 1}}
    #     response = get_stake_for_request_handler(event=event, context=None)
    #     assert (response["statusCode"] == 200)
    #     response_body = json.loads(response["body"])
    #     assert (response_body["status"] == "success")
    #     assert (response_body["data"] == [
    #         {'stake_member': '0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC', 'stake_amount': 100,
    #          'claim_back_amount': 60},
    #         {'stake_member': '0x3E5e9111Ae8eB78Fe1CC3bb8915d5D461F3Ef9A9', 'stake_amount': 150,
    #          'claim_back_amount': 90}])
    #
    # @patch("common.utils.Utils.report_slack")
    # def test_get_solution_for_given_request_id(self, mock_report_slack):
    #     event = {"resource": "/request/1/solution", "httpMethod": "GET",
    #              "pathParameters": {"request_id": 1}}
    #     response = get_solution_for_request_handler(event=event, context=None)
    #     assert (response["statusCode"] == 200)
    #     response_body = json.loads(response["body"])
    #     assert (response_body["status"] == "success")
    #     print(response_body)
    #     assert (response_body["data"] == [
    #         {'rfai_solution_id': 1, 'submitter': '0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b',
    #          'doc_uri': 'https://beta.singularitynet/service1', 'claim_amount': 10},
    #         {'rfai_solution_id': 2, 'submitter': '0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d',
    #          'doc_uri': 'https://beta.singularitynet/service2', 'claim_amount': 0}])
    #
    # @patch("common.utils.Utils.report_slack")
    # def test_get_foundation_members(self, mock_report_slack):
    #     event = {"resource": "/foundationmembers", "httpMethod": "GET"}
    #     response = get_foundation_members_handler(event=event, context=None)
    #     print(response)
    #     assert (response["statusCode"] == 200)
    #     response_body = json.loads(response["body"])
    #     assert (response_body["status"] == "success")
    #     print(response_body)
    #     assert (response_body["data"] == [{'member_id': 1, 'member_address': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc', 'status': 1}])

    @patch("common.utils.Utils.report_slack")
    def test_get_rfai_summary(self, mock_report_slack):
        event = {"resource": "/summary", "httpMethod": "GET"}
        response = rfai_summary_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")
        assert (response_body["data"] == [{'status': 'OPEN', 'request_count': 1}] )

