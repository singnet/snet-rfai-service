from enum import Enum


class RFAIStatus(Enum):
    OPEN = 0
    APPROVED = 1
    REJECTED = 2
    COMPLETED = 3
    CLOSED = 4
    COMPLETEDFROMUI = 555
    EXPIRED = 999
