class FundRequestTransactionDAO:
    def __init__(self, repo):
        self.repo = repo

    def persist_transaction(self, stake_member, transaction_hash, created_at):
        query_response = self.repo.execute(
            "INSERT INTO fund_request_transaction (stake_member, transaction_hash, created_at, row_created, row_updated) "
            "VALUES (%s, %s, %s, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)",
            [stake_member, transaction_hash, created_at])
        return query_response
