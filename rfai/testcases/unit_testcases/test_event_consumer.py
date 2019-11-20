import unittest
from unittest.mock import patch, Mock

from common.repository import Repository
from rfai.config import NETWORK_ID, NETWORK, IPFS_URL
from rfai.consumers.rfai_request_event_consumer import RFAICreateRequestEventConsumer, RFAIFundRequestEventConsumer
from rfai.dao.request_data_access_object import RequestDAO


class TestOrganizationEventConsumer(unittest.TestCase):
    def setUp(self):
        pass

    def test_rfai_create_request_event_consumer(self):
        _connection = Repository(NETWORKS=NETWORK)
        _rfai_request_repository = RequestDAO(_connection)

        event = {"data": {
            "row_id": 6,
            "block_no": 6774260,
            "event": "CreateRequest",
            "json_str": "{'requester': '0xFFcf8FDEE72ac11b5c542428B35EEF5769C409f0', 'requestId': 4, 'expiration': 7346080, 'amount': 100000000, 'documentURI': b'Qmcg1puzaupTUuSKsP773J8HPCekYHe9SGe5fBdjNb5Vjx'}",
            "processed": 0,
            "transactionHash": "b'\\x99\\x10\\xf4\\xf9\\xbfK\\n\\xedTo\\x89\\xefW.q\\xf2\\x9e.\\x9e\\x1dPh4{\\x88`\\x82\\xc6X\\xe6,T'",
            "logIndex": "25",
            "error_code": 0,
            "error_msg": "",
            "row_updated": "2019-11-18 14:52:55",
            "row_created": "2019-11-18 14:52:55"
        }, "name": "CreateRequest"}

        rfai_metadat = '{"title": "Autonomous AI Infra", "description": "Autonomous AI Infra for inference", "documentURI": "https://github.com/ksridharbabuus/A1", "training-dataset": "https://github.com/ksridharbabuus/A1", "acceptance-criteria": "Working solution in marketplace in given time", "created": "2019-11-14"}'
        #RFAICreateRequestEventConsumer().on_event(event)
        RFAICreateRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)

    def test_rfai_fund_request_event_consumer(self):
        event = {"data": {
            "row_id": 18,
            "block_no": 6777634,
            "event": "FundRequest",
            "json_str": "{'requestId': 2, 'staker': '0x9c302750c50307D3Ad88eaA9a6506874a15cE4Cb', 'amount': 100000000}",
            "processed": 0,
            "transactionHash": "b\"\\xea\\x9a\\xbc]\\x84\\x83<3\\xb7\\xf7n)\\xe3\\x8e*\\x85\\xc9\\x89\\xaf^R\\xcf[\\xa2'l\\xeb\\xc5\\xc8\\x8f\\xfb\\xaa\"",
            "logIndex": "19",
            "error_code": 0,
            "error_msg": "",
            "row_updated": "2019-11-18 14:53:03",
            "row_created": "2019-11-18 14:53:03"
        }, "name": "FundRequest"}

        block_chain_result = [True, 2, '0xC4f3BFE7D69461B7f363509393D44357c084404c', 900000000,
                              b'QmQBXqzR3Ckm1BZT19L1FeotE8jn6nzvaFn3HTLvtYYi85', 7345771, 6794369, 6824369, 1,
                              ['0xC4f3BFE7D69461B7f363509393D44357c084404c',
                               '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc',
                               '0x9c302750c50307D3Ad88eaA9a6506874a15cE4Cb'],
                              ['0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d']]

        RFAIFundRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)

    def extend_request_event_Consumer(self):
        # no events
        pass

    def approve_request_event_consumer(self):
        event = {
            "row_id": 7,
            "block_no": 6773958,
            "event": "ApproveRequest",
            "json_str": "{'requestId': 0, 'approver': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc', 'endSubmission': 6793941, 'endEvaluation': 6813941, 'expiration': 7301624}",
            "processed": 0,
            "transactionHash": "b'\\x7f2\\xb1\\xb1G`%\\x16\\xc3\\x03\\xedB:G%1B\\xf0\\xb91\\x08\\xab]\\xf6\\x9f\\n\\xd4i\\xa6\\xd28\\xb3'",
            "logIndex": "20",
            "error_code": 0,
            "error_msg": "",
            "row_updated": "2019-11-18 14:52:56",
            "row_created": "2019-11-18 14:52:56"
        }
        pass

    def add_foundation_memeber_event_consumer(self):
        event = {
            "row_id": 1,
            "block_no": 6773900,
            "event": "AddFoundationMember",
            "json_str": "{'member': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc', 'actor': '0x2e9c6C4145107cD21fCDc7319E4b24a8FF636c6B', 'role': 1, 'status': True}",
            "processed": 0,
            "transactionHash": "b'\\xa0\\xa0n\\xfe$\\x7f\\xbcL\\x81\\x91\\x19&\\xa2L\\r\\t\\x05o\\xc0\\x96\\x13\\x12\\rI]\\xff<@\\xa5W{\\xe3'",
            "logIndex": "1",
            "error_code": 0,
            "error_msg": "",
            "row_updated": "2019-11-18 14:52:52",
            "row_created": "2019-11-18 14:52:52"
        }

        pass

    def add_solution_request_event_consumer(self):
        event = {
            "row_id": 19,
            "block_no": 6774405,
            "event": "AddSolutionRequest",
            "json_str": "{'requestId': 0, 'submitter': '0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b', 'solutionDocURI': b'https:\/\/github.com\/tna3'}",
            "processed": 0,
            "transactionHash": "b'Z\\xb2y\\x17\\xc8\\tx \\x161\\xfe\\xfdL\\xc6Z\\x9a\\x19\\x0e\\xa7\\x08\\xb1W\\x1cb!0c\\xc4\\xa8\\xd8\\x9d6'",
            "logIndex": "55",
            "error_code": 0,
            "error_msg": "",
            "row_updated": "2019-11-18 14:53:03",
            "row_created": "2019-11-18 14:53:03"
        }

    def reject_request_event_consumer(self):
        event = {
            "row_id": 22,
            "block_no": 6773937,
            "event": "RejectRequest",
            "json_str": "{'requestId': 1, 'actor': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc'}",
            "processed": 0,
            "transactionHash": "b'l\\xd6\\x11h\\x8f\\xaa\\xb7\\x9b\\xb1\\x82\\x1fC\\xaa\\xb4\\xa0\\xc3\\xfcN\\xb7\\xe6\\xb9\\xab\\xec~\\x9c+2:\\x07\\x19\\xf5('",
            "logIndex": "2",
            "error_code": 0,
            "error_msg": "",
            "row_updated": "2019-11-18 14:53:05",
            "row_created": "2019-11-18 14:53:05"
        }

        pass


if __name__ == '__main__':
    unittest.main()