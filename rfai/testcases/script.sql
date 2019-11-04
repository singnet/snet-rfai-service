INSERT INTO service_request
(request_id, requester, fund_total, documentURI, expiration, end_submission, end_evaluation, status, request_title,
requester_name, description, git_hub_link, training_data_set_uri, acceptance_criteria, request_actor, row_created, row_updated)
VALUES(1, '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 100, '0xf15BB7b899250a67C02fcEDA18706B79aC997884', 123456, 123457, 123458, 0, 'Face Recognition', 'Dummy', 'Detecting faces from various perspective.', 'http://www.dummy.io/repo', '0xg15BB7b899250a67C02fcEDA18706B79aC997884', 'This is dummy . All are invited.', 'Dummy Actor', current_timestamp, current_timestamp);

INSERT INTO rfai_stake (request_id, stake_member, stake_amount, claim_back_amount, row_created, row_updated)
VALUES(1, '0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC', 100, 60, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);


INSERT INTO rfai_stake (request_id, stake_member, stake_amount, claim_back_amount, row_created, row_updated)
VALUES(1, '0x3E5e9111Ae8eB78Fe1CC3bb8915d5D461F3Ef9A9', 150, 90, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO rfai_solution (request_id, submitter, doc_uri, claim_amount, row_created, row_updated)
VALUES(1, '0x22d491Bde2303f2f43325b2108D26f1eAbA1e32b', 'https://beta.singularitynet/service1', 10, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO rfai_vote (request_id, voter_solution, rfai_solution_id, row_created, row_updated)
VALUES(1, '0x95cED938F7991cd0dFcb48F0a06a40FA1aF46EBC', 1, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

INSERT INTO rfai_vote (request_id, voter_solution, rfai_solution_id, row_created, row_updated)
VALUES(1, '0xd03ea8624C8C5987235048901fB614fDcA89b117', 2, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);