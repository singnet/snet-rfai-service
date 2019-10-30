-- --------------------------------------------------
create Table `service_request` (
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
	`row_created`	timestamp NULL DEFAULT NULL,
  	`row_updated` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  	PRIMARY KEY (`row_id`)
  	) ;
-- --------------------------------------------------