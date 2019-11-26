import unittest
import web3
from web3 import Web3
from common.repository import Repository
from rfai.config import NETWORK, IPFS_URL
from rfai.consumers.rfai_request_event_consumer import RFAIExtendRequestEventConsumer, \
    RFAIAddSolutionRequestEventConsumer, RFAIRejectRequestEventConsumer, RFAIAddFoundationMemberEventConsumer, \
    RFAIApproveRequestEventConsumer, RFAIFundRequestEventConsumer, RFAICreateRequestEventConsumer, RFAICloseRequestEventConsumer, RFAIVoteRequestEventConsumer
from rfai.dao.request_data_access_object import RequestDAO


def add_foundation_member_event_consumer():
    event = {"data": {
        "row_id": 1,
        "block_no": 6773900,
        "event": "AddFoundationMember",
        "json_str": "{'member': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc', 'actor': "
                    "'0x2e9c6C4145107cD21fCDc7319E4b24a8FF636c6B', 'role': 1, 'status': True}",
        "processed": 0,
        "transactionHash": "b'\\xa0\\xa0n\\xfe$\\x7f\\xbcL\\x81\\x91\\x19&\\xa2L\\r\\t\\x05o\\xc0\\x96\\x13\\x12\\rI"
                           "]\\xff<@\\xa5W{\\xe3'",
        "logIndex": "1",
        "error_code": 0,
        "error_msg": "",
        "row_updated": "2019-11-18 14:52:52",
        "row_created": "2019-11-18 14:52:52"
    }, "name": "AddFoundationMember"}

    RFAIAddFoundationMemberEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)


class TestOrganizationEventConsumer(unittest.TestCase):
    def setUp(self):
        pass

    # def test_rfai_create_request_event_consumer(self):
    #     _connection = Repository(NETWORKS=NETWORK)
    #     _rfai_request_repository = RequestDAO(_connection)
    #
    #     event = {"data": {
    #         "row_id": 6,
    #         "block_no": 6774260,
    #         "event": "CreateRequest",
    #         "json_str": "{'requester': '0xFFcf8FDEE72ac11b5c542428B35EEF5769C409f0', 'requestId': 4, 'expiration': "
    #                     "7346080, 'amount': 100000000, 'documentURI': "
    #                     "b'Qmcg1puzaupTUuSKsP773J8HPCekYHe9SGe5fBdjNb5Vjx'}",
    #         "processed": 0,
    #         "transactionHash": "b'\\x99\\x10\\xf4\\xf9\\xbfK\\n\\xedTo\\x89\\xefW.q\\xf2\\x9e.\\x9e\\x1dPh4{"
    #                            "\\x88`\\x82\\xc6X\\xe6,T'",
    #         "logIndex": "25",
    #         "error_code": 0,
    #         "error_msg": "",
    #         "row_updated": "2019-11-18 14:52:55",
    #         "row_created": "2019-11-18 14:52:55"
    #     }, "name": "CreateRequest"}
    #
    #     rfai_metadat = '{"title": "Autonomous AI Infra", "description": "Autonomous AI Infra for inference", ' \
    #                    '"documentURI": "https://github.com/ksridharbabuus/A1", "training-dataset": ' \
    #                    '"https://github.com/ksridharbabuus/A1", "acceptance-criteria": "Working solution in ' \
    #                    'marketplace in given time", "created": "2019-11-14"} '
    #     RFAICreateRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)
    #
    # def test_rfai_fund_request_event_consumer(self):
    #     event = {"data": {
    #         "row_id": 18,
    #         "block_no": 6777634,
    #         "event": "FundRequest",
    #         "json_str": "{'requestId': 4, 'staker': '0x9c302750c50307D3Ad88eaA9a6506874a15cE4Cb', 'amount': 100000000}",
    #         "processed": 0,
    #         "transactionHash": "b\"\\xea\\x9a\\xbc]\\x84\\x83<3\\xb7\\xf7n)\\xe3\\x8e*\\x85\\xc9\\x89\\xaf^R\\xcf["
    #                            "\\xa2'l\\xeb\\xc5\\xc8\\x8f\\xfb\\xaa\"",
    #         "logIndex": "19",
    #         "error_code": 0,
    #         "error_msg": "",
    #         "row_updated": "2019-11-18 14:53:03",
    #         "row_created": "2019-11-18 14:53:03"
    #     }, "name": "FundRequest"}
    #
    #     block_chain_result = [True, 2, '0xC4f3BFE7D69461B7f363509393D44357c084404c', 900000000,
    #                           b'QmQBXqzR3Ckm1BZT19L1FeotE8jn6nzvaFn3HTLvtYYi85', 7345771, 6794369, 6824369, 1,
    #                           ['0xC4f3BFE7D69461B7f363509393D44357c084404c',
    #                            '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc',
    #                            '0x9c302750c50307D3Ad88eaA9a6506874a15cE4Cb'],
    #                           ['0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d']]
    #
    #     RFAIFundRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)

    # def extend_request_event_Consumer(self):
    #     event = {"data": {
    #         "row_id": 23,
    #         "block_no": 6812889,
    #         "event": "ExtendRequest",
    #         "json_str": "{'requestId': 4, 'requester': '0xFFcf8FDEE72ac11b5c542428B35EEF5769C409f0', 'expiration': "
    #                     "7348080}",
    #         "processed": 1,
    #         "transactionHash": "b'\\x1c\\x1e\\xb98\\xaa7W\\xb5J\\xb5\\xab\\xee^\\xe7\\x95\\xce\\x13\\x08\\x86\\x8a"
    #                            "\\x1c\\xc9\\x19\\xe1SE\\xf9\\xb2Z\\xc1X\\xb7'",
    #         "logIndex": "49",
    #         "error_code": 200,
    #         "error_msg": "",
    #         "row_updated": "2019-11-20 13:16:25",
    #         "row_created": "2019-11-20 13:16:25"
    #     }, "name": "ExtendRequest"}
    #
    #     RFAIExtendRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)
    #
    # def test_approve_request_event_consumer(self):
    #     event = {"data": {
    #         "row_id": 7,
    #         "block_no": 6773958,
    #         "event": "ApproveRequest",
    #         "json_str": "{'requestId': 4, 'approver': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc', 'endSubmission': "
    #                     "6793941, 'endEvaluation': 6813941, 'expiration': 7301624}",
    #         "processed": 0,
    #         "transactionHash": "b'\\x7f2\\xb1\\xb1G`%\\x16\\xc3\\x03\\xedB:G%1B\\xf0\\xb91\\x08\\xab]\\xf6\\x9f\\n"
    #                            "\\xd4i\\xa6\\xd28\\xb3'",
    #         "logIndex": "20",
    #         "error_code": 0,
    #         "error_msg": "",
    #         "row_updated": "2019-11-18 14:52:56",
    #         "row_created": "2019-11-18 14:52:56"
    #     }, "name": "ApproveRequest"}
    #     RFAIApproveRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)
    #
    # def test_add_solution_request_event_consumer(self):
    #     event = {
    #         "data": {
    #             "row_id": 19,
    #             "block_no": 6774405,
    #             "event": "AddSolutionRequest",
    #             "json_str": "{'requestId': 1, 'submitter': '0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b', "
    #                         "'solutionDocURI': b'https:\/\/github.com\/tna3'}",
    #             "processed": 0,
    #             "transactionHash": "b'Z\\xb2y\\x17\\xc8\\tx \\x161\\xfe\\xfdL\\xc6Z\\x9a\\x19\\x0e\\xa7\\x08\\xb1W"
    #                                "\\x1cb!0c\\xc4\\xa8\\xd8\\x9d6'",
    #             "logIndex": "55",
    #             "error_code": 0,
    #             "error_msg": "",
    #             "row_updated": "2019-11-18 14:53:03",
    #             "row_created": "2019-11-18 14:53:03"
    #         }
    #     }
    #     RFAIAddSolutionRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(
    #         event)
    #
    # def test_reject_request_event_consumer(self):
    #     event = {
    #         "data": {
    #             "row_id": 22,
    #             "block_no": 6773937,
    #             "event": "RejectRequest",
    #             "json_str": "{'requestId': 1, 'actor': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc'}",
    #             "processed": 0,
    #             "transactionHash": "b'l\\xd6\\x11h\\x8f\\xaa\\xb7\\x9b\\xb1\\x82\\x1fC\\xaa\\xb4\\xa0\\xc3\\xfcN\\xb7"
    #                                "\\xe6\\xb9\\xab\\xec~\\x9c+2:\\x07\\x19\\xf5('",
    #             "logIndex": "2",
    #             "error_code": 0,
    #             "error_msg": "",
    #             "row_updated": "2019-11-18 14:53:05",
    #             "row_created": "2019-11-18 14:53:05"
    #         }
    #     }
    #     RFAIRejectRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)

    def test_close_request_event_consumer(self):
        event = {"data": {
            "row_id": 37,
            "block_no": 6843329,
            "event": "CloseRequest",
            "json_str": "{'requestId': 8, 'actor': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc'}",
            "processed": 1,
            "transactionHash": "b'V$u0\\xdc\\x18\\x02X&|\\xde,"
                               ">\\x9c|\\xc7\\xa4\\xf9\\xcb\\x00\\xebX!\\x88]\\x9bM\\xbf62\\x9b\\xf6'",
            "logIndex": "0",
            "error_code": 200,
            "error_msg": "",
            "row_updated": "2019-11-25 07:26:25",
            "row_created": "2019-11-25 07:26:25"
        }}
        RFAICloseRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)

    def test_vote_request_event_consumer(self):
        event = {"data": {
            "row_id": 35,
            "block_no": 6843313,
            "event": "VoteRequest",
            "json_str": "{'requestId': 6, 'voter': '0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc', 'submitter': "
                        "'0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC'}",
            "processed": 1,
            "transactionHash": "b'8?}\\x9e\\x08\/Q\\xae\\x99\\x15\\x81\\xd9G\\x95\\x01\\xe7\\xfb\\x1d\\x89d,"
                               "\\xfc\\x19\\x99\\xb9\\xb2H\\xf6w3\\xf2k'",
            "logIndex": "20",
            "error_code": 200,
            "error_msg": "",
            "row_updated": "2019-11-25 07:20:25",
            "row_created": "2019-11-25 07:20:25"
        }}
        RFAIVoteRequestEventConsumer(3, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(event)

    # def test_claim_back_request_event_consumer(self):
    #     event = {"data": {
    #         "row_id": 39,
    #         "block_no": 6843438,
    #         "event": "ClaimBackRequest",
    #         "json_str": "{'requestId': 8, 'stacker': '0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1', 'amount': 200000000}",
    #         "processed": 1,
    #         "transactionHash": "b'\\xda\\xa3\\xb7\\xb0K\\xaa6\\x94\\xb1\\xc9\\x03["
    #                            "\\xc4\\x04\\x99D\\xde\\x85\\xe1\\xccS\\xb5Z\\x91\\x9a\\x8f\\xad\\xf3\\xb6\\xcf\\xf3"
    #                            "\\xed'",
    #         "logIndex": "13",
    #         "error_code": 200,
    #         "error_msg": "",
    #         "row_updated": "2019-11-25 07:56:25",
    #         "row_created": "2019-11-25 07:56:25"
    #     }}
    #
    # def test_claim_request_event_consumer(self):
    #     event = {"data": {
    #         "row_id": 41,
    #         "block_no": 6843627,
    #         "event": "ClaimRequest",
    #         "json_str": "{'requestId': 6, 'submitter': '0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC', 'amount': "
    #                     "200000000}",
    #         "processed": 1,
    #         "transactionHash": "b'i\\\\Z&5Z\\xb8\\x18\\xff\\x10\\x0e\\x9e\\xfbe\\x86\\x88.\\x14\\xcd!Qv\\x00\\x836"
    #                            "\\xfa\\xea\\xed\\x0eE\\xf4l'",
    #         "logIndex": "12",
    #         "error_code": 200,
    #         "error_msg": "",
    #         "row_updated": "2019-11-25 08:36:25",
    #         "row_created": "2019-11-25 08:36:25"
    #     }}


if __name__ == '__main__':
    unittest.main()