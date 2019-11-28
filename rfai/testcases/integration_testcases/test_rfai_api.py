import json
import unittest
from unittest.mock import patch

from rfai.requests_for_ai_handler import get_vote_for_request_handler, rfai_summary_handler, \
    get_stake_for_request_handler, get_solution_for_request_handler, get_foundation_members_handler, request_handler, \
    get_claim_for_solution_provider_handler, get_claim_for_stakers_handler

from rfai.rfai_status import RFAIStatusCodes


class TestRFAIAPI(unittest.TestCase):
    def setUp(self):
        pass

    @patch("common.utils.Utils.report_slack")
    def test_get_request_for_pending_status(self, mock_report_slack):
        event = {"resource": "/request", "httpMethod": "GET",
                 "queryStringParameters": {"requester": "0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc",
                                           "my_request": "False",
                                           "status": "pending"}}
        response = request_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")
        assert (response_body["data"] == [{'request_id': 1, 'requester': '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 'request_fund': 100, 'fund_total': 100, 'documentURI': '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 'expiration': 7348080, 'end_submission': 123457, 'end_evaluation': 123458, 'status': 0, 'request_title': 'Face Recognition', 'requester_name': 'Dummy', 'description': 'Detecting faces from various perspective.', 'git_hub_link': 'http://www.dummy.io/repo', 'training_data_set_uri': '0xg15BB7b899250a67C02fcEDA18706B79aC997884', 'acceptance_criteria': 'This is dummy . All are invited.', 'request_actor': 'Dummy Actor', 'created_at': '2019-11-04 17:34:28', 'vote_count': 2, 'stake_count': 2, 'solution_count': 2}])

    @patch("common.utils.Utils.report_slack")
    def test_get_request_for_solution_vote_status(self, mock_report_slack):
        event = {"resource": "/request", "httpMethod": "GET",
                 "queryStringParameters": {"requester": "0xf15BB7b899250a67C02fcEDA18706B79aC997884",
                                           "status": "solution_vote"}}
        response = request_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        print(response_body)
        assert (response_body["status"] == "success")
        assert (response_body["data"] == [{'request_id': 2, 'requester': '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 'request_fund': 100, 'fund_total': 100, 'documentURI': '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 'expiration': 7348080, 'end_submission': 123457, 'end_evaluation': 7248080, 'status': 1, 'request_title': 'Face Recognition', 'requester_name': 'Dummy', 'description': 'Detecting faces from various perspective.', 'git_hub_link': 'http://www.dummy.io/repo', 'training_data_set_uri': '0xg15BB7b899250a67C02fcEDA18706B79aC997884', 'acceptance_criteria': 'This is dummy . All are invited.', 'request_actor': 'Dummy Actor', 'created_at': '2019-11-04 17:34:28', 'vote_count': 0, 'stake_count': 0, 'solution_count': 0}])

    @patch("common.utils.Utils.report_slack")
    def test_get_vote_for_given_request_id(self, mock_report_slack):
        event = {"resource": "/request/1/vote", "httpMethod": "GET",
                 "pathParameters": {"requestId": 1}}
        response = get_vote_for_request_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        print(response_body)
        assert (response_body["status"] == "success")
        assert (response_body["data"] == [
            {"voter": "0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC", "created_at": "2019-11-04 17:34:28",
             "submitter": "0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b"},
            {"voter": "0xd03ea8624C8C5987235048901fB614fDcA89b117", "created_at": "2019-11-04 17:34:28",
             "submitter": "0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d"}])

    @patch("common.utils.Utils.report_slack")
    def test_get_stake_for_given_request_id(self, mock_report_slack):
        event = {"resource": "/request/1/stake", "httpMethod": "GET",
                 "pathParameters": {"requestId": 1}}
        response = get_stake_for_request_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")
        assert (response_body["data"] == [
            {'stake_member': '0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC', 'stake_amount': 100, 'claim_back_amount': 60,
             'created_at': '2019-11-04 17:34:28'},
            {'stake_member': '0x3E5e9111Ae8eB78Fe1CC3bb8915d5D461F3Ef9A9', 'stake_amount': 150, 'claim_back_amount': 90,
             'created_at': '2019-11-04 17:34:28'}])

    @patch("common.utils.Utils.report_slack")
    def test_get_solution_for_given_request_id(self, mock_report_slack):
        event = {"resource": "/request/1/solution", "httpMethod": "GET",
                 "pathParameters": {"requestId": 1}}
        response = get_solution_for_request_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")
        assert (response_body["data"] == [
            {'rfai_solution_id': 1, 'submitter': '0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b',
             'doc_uri': 'https://beta.singularitynet/service1', 'claim_amount': 10,
             'created_at': '2019-11-04 17:34:28'},
            {'rfai_solution_id': 2, 'submitter': '0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d',
             'doc_uri': 'https://beta.singularitynet/service2', 'claim_amount': 0,
             'created_at': '2019-11-04 17:34:28'}])

    @patch("common.utils.Utils.report_slack")
    def test_get_foundation_members(self, mock_report_slack):
        event = {"resource": "/foundationmembers", "httpMethod": "GET"}
        response = get_foundation_members_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")
        assert (response_body["data"][0]["member_address"] == "0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc")
        assert (response_body["data"][0]["role"] == 0)
        assert (response_body["data"][0]["status"] == 1)

    @patch("common.utils.Utils.report_slack")
    def test_get_rfai_summary(self, mock_report_slack):
        event = {"resource": "/summary",
                 "httpMethod": "GET",
                 "queryStringParameters": {"requester": "0xf15BB7b899250a67C02fcEDA18706B79aC997884",
                                           "status": "solution_vote"}}
        response = rfai_summary_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")
        assert (response_body["data"]["PENDING"] == 1)
        assert (response_body["data"]["ACTIVE"] == 0)
        assert (response_body["data"]["SOLUTION_VOTE"] == 1)
        assert (response_body["data"]["COMPLETED"] == 0)
        assert (response_body["data"]["REJECTED"] == 0)
        assert (response_body["data"]["CLOSED"] == 0)

    @patch("common.utils.Utils.report_slack")
    def test_get_claims_data_for_solution_provider(self, mock_report_slack):
        event = {"resource": "/claim/submitter",
                 "httpMethod": "GET",
                 "queryStringParameters": {"user_address": "0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d"}}
        response = get_claim_for_solution_provider_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")
        assert (response_body["data"] == [
            {"row_id": 2, "request_id": 1, "request_title": "Face Recognition", "votes": 1, "expiration": 7348080,
             "tokens": 0, "end_evaluation": 123458}])

    @patch("common.utils.Utils.report_slack")
    def test_get_claims_data_for_stake_provider(self, mock_report_slack):
        event = {"resource": "/claim/stake",
                 "httpMethod": "GET",
                 "queryStringParameters": {"user_address": "0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b"}}
        response = get_claim_for_stakers_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")


if __name__ == '__main__':
    unittest.main()
