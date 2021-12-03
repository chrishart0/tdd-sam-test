import json
from hello_world import persistData

def save_employee(first_name, middle_name, last_name, id):
    employee_data = persistData.PersistData()

    for data in (first_name, last_name, id):
        if (data == ""):
            return {"is_recorded": False}

    if employee_data.retrieve_employee(id):
        return {"is_recorded": False}

    response = employee_data.persist_employee(first_name, middle_name, last_name, id)
    
    return response

def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    return {
        "statusCode": 200,
        "body": json.dumps(
            {
                "message": "hello world",
            }
        ),
    }
