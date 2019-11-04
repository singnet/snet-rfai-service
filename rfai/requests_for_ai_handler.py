from common.logger import get_logger
from common.repository import Repository
from common.utils import Utils
from rfai.config import NETWORK_ID, NETWORK, SLACK_HOOK
from rfai.constant import REQUIRED_KEYS_FOR_GET_RFAI_EVENT
from rfai.service.rfai_service import RFAIService

rfai = RFAIService(repo=Repository(NETWORKS=NETWORK))
util = Utils()
logger = get_logger(__name__)


def request_handler(event, context):
    try:
        logger.info(event)
        valid_event = util.validate_dict(
            data_dict=event, required_keys=REQUIRED_KEYS_FOR_GET_RFAI_EVENT)
        if not valid_event:
            return util.generate_lambda_response(400, "Bad Request", cors_enabled=True)
        query_string_parameters = event["queryStringParameters"]
        response_data = rfai.get_requests(status=query_string_parameters["status"],
                                          requester=query_string_parameters["requester"])
        response = util.generate_lambda_response(200, {"status": "success", "data": response_data}, cors_enabled=True)
    except Exception as e:
        error_message = util.format_error_message(
            status="failed",
            error=repr(e),
            payload=query_string_parameters,
            net_id=NETWORK_ID,
            handler="get-rfai"
        )
        util.report_slack(error_message, SLACK_HOOK)
        response = util.generate_lambda_response(500, error_message, cors_enabled=True)
    return response
