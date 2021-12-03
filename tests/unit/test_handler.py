import json

import pytest

from hello_world import app


@pytest.fixture()
def apigw_event():
    """ Generates API GW Event"""

    return {
        "body": '{ "test": "body"}',
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "queryStringParameters": {"foo": "bar"},
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "pathParameters": {"proxy": "/examplepath"},
        "httpMethod": "POST",
        "stageVariables": {"baz": "qux"},
        "path": "/examplepath",
    }


def test_lambda_handler(apigw_event, mocker):

    ret = app.lambda_handler(apigw_event, "")
    data = json.loads(ret["body"])

    assert ret["statusCode"] == 200
    assert "message" in ret["body"]
    assert data["message"] == "hello world"

def test_given_valid_employee_data_when_save_employee_then_employee_presisted(apigw_event, mocker):

    # arrange
    first_name = "Josef"
    last_name = "Butts"
    middle_name = "Likes"
    id = "1"

    # act
    save_response = app.save_employee(first_name, middle_name, last_name, id )

    # assert
    assert save_response["is_recorded"] == True

def test_given_no_first_name_employee_data_when_save_employee_then_employee_not_presisted(apigw_event, mocker):

    # arrange
    first_name = ""
    last_name = "Butts"
    middle_name = "Likes"
    id = "1"

    # act
    save_response = app.save_employee(first_name, middle_name, last_name, id )

    # assert
    assert save_response["is_recorded"] == False

def test_given_no_last_name_employee_data_when_save_employee_then_employee_not_presisted(apigw_event, mocker):

    # arrange
    first_name = "Josef"
    last_name = ""
    middle_name = "Likes"
    id = "1"

    # act
    save_response = app.save_employee(first_name, middle_name, last_name, id )

    # assert
    assert save_response["is_recorded"] == False

def test_given_no_id_employee_data_when_save_employee_then_employee_not_presisted(apigw_event, mocker):

    # arrange
    first_name = "Josef"
    last_name = "Butts"
    middle_name = "Likes"
    id = ""

    # act
    save_response = app.save_employee(first_name, middle_name, last_name, id )

    # assert
    assert save_response["is_recorded"] == False

def test_given_existing_id_employee_data_when_save_employee_then_employee_not_presisted(apigw_event, mocker):

    # arrange
    first_name = "Josef"
    last_name = "Butts"
    middle_name = "Likes"
    id = "1"

    # act
    app.save_employee(first_name, middle_name, last_name, id)
    save_response = app.save_employee(first_name, middle_name, last_name, id)

    # assert
    assert save_response["is_recorded"] == False