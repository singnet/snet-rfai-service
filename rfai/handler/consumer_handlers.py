from common.constant import StatusCode
from common.logger import get_logger
from common.utils import Utils
from rfai.config import SLACK_HOOK
# from rfai.consumers.consumer_factory import get_create_request_event_consumer
logger = get_logger(__name__)
util = Utils()


def create_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Create Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))
