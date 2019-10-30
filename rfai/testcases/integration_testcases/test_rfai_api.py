import json
import unittest
from unittest.mock import patch

from rfai.requests_for_ai_handler import request_handler


class TestRFAIAPI(unittest.TestCase):
    def setUp(self):
        pass

    @patch("common.utils.Utils.report_slack")
    def test_get_request_for_given_requester(self, mock_report_slack):
        event = {"resource": "/request", "httpMethod": "GET",
                 "queryStringParameters": {"requester": "0xf15BB7b899250a67C02fcEDA18706B79aC997884", "status": "Open"}}
        response = request_handler(event=event, context=None)
        assert (response["statusCode"] == 200)
        response_body = json.loads(response["body"])
        assert (response_body["status"] == "success")
        assert (response_body["data"] == [
            {'request_id': 1, 'requester': '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 'fund_total': 100,
             'documentURI': '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 'expiration': 123456,
             'end_submission': 123457, 'end_evaluation': 123458, 'status': 0, 'request_title': 'Face Recognition',
             'requester_name': 'Dummy', 'description': 'Detecting faces from various perspective.',
             'git_hub_link': 'http://www.dummy.io/repo',
             'training_data_set_uri': '0xg15BB7b899250a67C02fcEDA18706B79aC997884',
             'acceptance_criteria': 'This is dummy . All are invited.', 'request_actor': 'Dummy Actor'}])
