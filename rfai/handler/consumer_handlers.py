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
        print(event)
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def extend_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Extend Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def approve_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Approve Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def fund_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Fund Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def add_solution_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Add Solution Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def vote_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Vote Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def claim_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Claim Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def close_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Close Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def reject_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Reject Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def claim_back_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Claim Back Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def add_foundation_member_consumer_handler(event, context):
    try:
        logger.info(f"Got Add Foundation Member Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(200, StatusCode.OK)
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))