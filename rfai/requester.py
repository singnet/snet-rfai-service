class Requester:
    def __init__(self, request_id, requester, expiration, amount, document_uri):
        self.request_id = request_id
        self.requester = requester
        self.expiration = expiration
        self.amount = amount
        self.document_uri = document_uri
