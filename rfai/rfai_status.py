from enum import Enum


class ApprovedRequestStatus(Enum):
    ACTIVE = "APPROVED/ACTIVE"
    SOLUTION_VOTE = "APPROVED/SOLUTION_VOTE"
    COMPLETED = "APPROVED/COMPLETED"
    EXPIRED = "APPROVED/EXPIRED"


class OpenRequestStatus(Enum):
    ACTIVE = "OPEN/ACTIVE"
    EXPIRED = "OPEN/EXPIRED"


class RFAIStatus(Enum):
    OPEN = OpenRequestStatus
    APPROVED = ApprovedRequestStatus


class RFAIStatusCodes(Enum):
    OPEN = 0
    APPROVED = 1
    REJECTED = 2
    CLOSED = 4
