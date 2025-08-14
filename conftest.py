import pytest
import requests

# Get an authentication token for API requests, obsolete, use token.get() instead
@pytest.fixture(scope='session')
def get_auth_token():
    url="https://qv77wuaaytru4gzchjj7bhewhq0ukysc.lambda-url.us-west-2.on.aws/auth"
    payload = {"apiKey": "test-key-001"}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json().get("token")
    #todo handle expired token
