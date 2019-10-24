def request_handler(event, context):
    try:
        # valid_event = validate_dict(
        #     data_dict=event, required_keys=REQUIRED_KEYS_FOR_GET_RFAI_EVENT)
        # if not valid_event:
        #     return generate_lambda_response(400, "Bad Request", cors_enabled=True)
        print(event)
        # response = generate_lambda_response(200, {"status": "success", "data": ""}, cors_enabled=True)
    except Exception as e:
        print(repr(e))