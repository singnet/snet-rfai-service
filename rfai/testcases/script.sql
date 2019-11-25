INSERT INTO service_request
(request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, status, request_title,
requester_name, description, git_hub_link, training_data_set_uri, acceptance_criteria, request_actor, created_at, row_created, row_updated)
VALUES(1, '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 100, '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 7348080, 123457, 123458, 0, 'Face Recognition', 'Dummy', 'Detecting faces from various perspective.', 'http://www.dummy.io/repo', '0xg15BB7b899250a67C02fcEDA18706B79aC997884', 'This is dummy . All are invited.', 'Dummy Actor', str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, current_timestamp);

INSERT INTO rfai_stake (request_id, stake_member, stake_amount, claim_back_amount, transaction_hash, created_at, row_created, row_updated)
VALUES(1, '0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC', 100, 60, "0xbfd83e85caa0942e1cd5497e9fb4902e7f1a853f8d6eda33823603067b88c38f", str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


INSERT INTO rfai_stake (request_id, stake_member, stake_amount, claim_back_amount, transaction_hash, created_at, row_created, row_updated)
VALUES(1, '0x3E5e9111Ae8eB78Fe1CC3bb8915d5D461F3Ef9A9', 150, 90, "0xafd83e85caa0942e1cd5497e9fb4902e7f1a853f8d6eda33823603067b88c38f", str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO rfai_solution (request_id, submitter, doc_uri, claim_amount, created_at, row_created, row_updated)
VALUES(1, '0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b', 'https://beta.singularitynet/service1', 10, str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO rfai_solution (request_id, submitter, doc_uri, claim_amount, created_at, row_created, row_updated)
VALUES(1, '0xE11BA2b4D45Eaed5996Cd0823791E0C93114882d', 'https://beta.singularitynet/service2', 0, str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO rfai_vote (request_id, voter_solution, rfai_solution_id, created_at, row_created, row_updated)
VALUES(1, '0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC', 1, str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO rfai_vote (request_id, voter_solution, rfai_solution_id, created_at, row_created, row_updated)
VALUES(1, '0xd03ea8624C8C5987235048901fB614fDcA89b117', 2, str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO foundation_member (member_address, role, status, request_actor, created_at, row_created, row_updated)
VALUES('0x3a1fe7E30D9e140f72870E6D74BF8d0c690A4dBc', 0, 1, '', str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO service_request
(request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, status, request_title,
requester_name, description, git_hub_link, training_data_set_uri, acceptance_criteria, request_actor, created_at, row_created, row_updated)
VALUES(2, '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 100, '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 7348080, 123457, 7248080, 1, 'Face Recognition', 'Dummy', 'Detecting faces from various perspective.', 'http://www.dummy.io/repo', '0xg15BB7b899250a67C02fcEDA18706B79aC997884', 'This is dummy . All are invited.', 'Dummy Actor', str_to_date('2019-11-04 17:34:28', '%Y-%m-%d %H:%i:%s'), CURRENT_TIMESTAMP, current_timestamp);
