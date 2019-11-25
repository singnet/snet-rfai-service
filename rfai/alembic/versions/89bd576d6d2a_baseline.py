"""baseline

Revision ID: 89bd576d6d2a
Revises:
Create Date: 2019-11-07 14:37:50.121706

"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '89bd576d6d2a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    conn = op.get_bind()
    conn.execute("""CREATE TABLE `service_request` (
            `row_id`        int(11) NOT NULL AUTO_INCREMENT,
            `request_id`	int(11) NOT NULL,
            `requester`	varchar(50) DEFAULT NULL,
            `fund_total`	int(11),
            `documentURI`	Varchar(255),
            `expiration`	int(11),
            `end_submission`	int(11),
            `end_evaluation`	int(11),
            `status`	int(4),
            `request_title`	varchar(255),
            `requester_name`	varchar(255),
            `description`	varchar(1024),
            `git_hub_link`	varchar(255),
            `training_data_set_uri`	Varchar(255),
            `acceptance_criteria`	varchar(1024),
            `request_actor`	varchar(50),
            `created_at`	timestamp NULL DEFAULT NULL,
            `row_created`	timestamp NULL DEFAULT NULL,
            `row_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`row_id`),
            UNIQUE KEY `uq_request` (`request_id`));
        """)
    conn.execute("""CREATE TABLE `foundation_member` (
            `row_id`        int(11) NOT NULL AUTO_INCREMENT,
            `member_address`	varchar(50) NOT NULL,
            `role`	bit(1),
            `status`	bit(1),
            `request_actor`	varchar(50) DEFAULT NULL,
            `created_at`	timestamp NULL DEFAULT NULL,
            `row_created`	timestamp NULL DEFAULT NULL,
            `row_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`row_id`),
            UNIQUE KEY `uq_member` (`member_address`));
        """)
    conn.execute("""CREATE TABLE `rfai_stake` (
            `row_id`        int(11) NOT NULL AUTO_INCREMENT,
            `request_id`	int(11) NOT NULL,
            `stake_member`	varchar(50) NOT NULL,
            `stake_amount`	int(20) NOT NULL,
            `claim_back_amount`	int(20) DEFAULT NULL,
            `transaction_hash`	varchar(100) NOT NULL,
            `created_at`	timestamp NULL DEFAULT NULL,
            `row_created`	timestamp NULL DEFAULT NULL,
            `row_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`row_id`),
            UNIQUE KEY `uq_txn_hash` (`transaction_hash`),
            CONSTRAINT `RFAIStakeRequestIdFK` FOREIGN KEY (`request_id`) REFERENCES `service_request` (`request_id`) ON DELETE CASCADE);
        """)
    conn.execute("""CREATE TABLE `rfai_solution` (
            `row_id`        int(11) NOT NULL AUTO_INCREMENT,
            `request_id`	int(11) NOT NULL,
            `submitter`	varchar(50) NOT NULL,
            `doc_uri`	varchar(255) NOT NULL,
            `claim_amount`	int(20) DEFAULT NULL,
            `created_at`	timestamp NULL DEFAULT NULL,
            `row_created`	timestamp NULL DEFAULT NULL,
            `row_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`row_id`),
            CONSTRAINT `RFAISolutionRequestIdFK` FOREIGN KEY (`request_id`) REFERENCES `service_request` (`request_id`) ON DELETE CASCADE);
        """)
    conn.execute("""CREATE TABLE `rfai_vote` (
            `row_id`        int(11) NOT NULL AUTO_INCREMENT,
            `request_id`	int(11) NOT NULL,
            `voter`	varchar(100) NOT NULL,
            `rfai_solution_id`	int(11),
            `created_at`	timestamp NULL DEFAULT NULL,
            `row_created`	timestamp NULL DEFAULT NULL,
            `row_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (`row_id`),
            UNIQUE KEY `uq_vote` (`voter`, `rfai_solution_id`),
            CONSTRAINT `RFAIVoteRequestIdFK` FOREIGN KEY (`request_id`) REFERENCES `service_request` (`request_id`) ON DELETE CASCADE,
            CONSTRAINT `RFAIVoteSolutionIdFK` FOREIGN KEY (`rfai_solution_id`) REFERENCES `rfai_solution` (`row_id`) ON DELETE CASCADE);
        """)


def downgrade():
    conn = op.get_bind()
    conn.execute("""DROP TABLE rfai_stake;""")
    conn.execute("""DROP TABLE rfai_solution;""")
    conn.execute("""DROP TABLE rfai_vote;""")
    conn.execute("""DROP TABLE service_request;""")
    conn.execute("""DROP TABLE foundationmembers;""")
