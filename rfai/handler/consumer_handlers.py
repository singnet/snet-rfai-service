from common.constant import StatusCode
from common.logger import get_logger
from common.utils import Utils
from rfai.config import SLACK_HOOK, NETWORK_ID, NETWORK, IPFS_URL
from rfai.consumers.rfai_request_event_consumer import RFAIApproveRequestEventConsumer, RFAICreateRequestEventConsumer

logger = get_logger(__name__)
util = Utils()


def rfai_create_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Create Request Event {event}")

        RFAICreateRequestEventConsumer(NETWORK_ID, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(
            event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_extend_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Extend Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_approve_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Approve Request Event {event}")
        RFAIApproveRequestEventConsumer(NETWORK_ID, NETWORK['ws_provider'], IPFS_URL['url'], IPFS_URL['port']).on_event(
            event)
        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_fund_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Fund Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_add_solution_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Add Solution Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_vote_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Vote Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_claim_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Claim Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_close_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Close Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_reject_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Reject Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_claim_back_request_consumer_handler(event, context):
    try:
        logger.info(f"Got Claim Back Request Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))


def rfai_add_foundation_member_consumer_handler(event, context):
    try:
        logger.info(f"Got Add Foundation Member Event {event}")
        # create_request_event_consumer = get_create_request_event_consumer(event)
        # create_request_event_consumer.on_event(event)

        return util.generate_lambda_response(StatusCode.OK, "Event processed")
    except Exception as e:
        logger.exception(f"error  {str(e)} while processing event {event}")
        util.report_slack("ERROR", f"got error : {str(e)} \n for event : {event}", SLACK_HOOK)

        return util.generate_lambda_response(500, str(e))
