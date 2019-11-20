from rfai.config import NETWORK, NETWORK_ID, IPFS_URL
from rfai.consumers.rfai_request_event_consumer import CreateRequestEventConsumer, \
    ExtendRequestEventConsumer, ApproveRequestEventConsumer


def get_create_request_event_consumer(event):
    if event['name'] == "CreateRequest":
        return CreateRequestEventConsumer(NETWORK[NETWORK_ID]["ws_provider"], IPFS_URL['url'],
                                          IPFS_URL['port'])
    elif event['name'] == 'ExtendRequest':
        return ExtendRequestEventConsumer(NETWORK[NETWORK_ID]["ws_provider"], IPFS_URL['url'],
                                          IPFS_URL['port'])
    elif event['name'] == "ApproveRequest":
        return ApproveRequestEventConsumer(NETWORK[NETWORK_ID]["ws_provider"], IPFS_URL['url'],
                                           IPFS_URL['port'])