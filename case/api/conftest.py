import pytest
import requests

@pytest.fixture()
def get_auth_token(scope='session'):
    url="https://qv77wuaaytru4gzchjj7bhewhq0ukysc.lambda-url.us-west-2.on.aws/auth"
    payload = {"apiKey": "test-key-001"}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json().get("token")
    #todo handle expired token
    #todo cache token