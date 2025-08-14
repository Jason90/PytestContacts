import requests
import pytest
from util import json_util



CONTACTS_URL = "https://qv77wuaaytru4gzchjj7bhewhq0ukysc.lambda-url.us-west-2.on.aws/contacts"
TIMEOUT=10

#todo token
def test_get_contacts(get_auth_token):
    # Step 1: Get the authentication token
	token= get_auth_token
	headers = {
		"Authorization": f"Bearer {token}"
	}
	# Step 2: Make the GET request to fetch contacts
	response = requests.get(CONTACTS_URL, headers=headers, timeout=TIMEOUT)	
	# Step 3: Validate the response status code
	assert response.status_code == 200
	contacts = response.json()	
	assert isinstance(contacts, list)
	assert len(contacts) > 0
	# Step 4: Validate the JSON structure against the schema
	schema = json_util.load_schema("data/schema/contacts_schema.json")
	try:
		assert json_util.validate_json(contacts, schema)
	except ValueError as e:
		pytest.fail(f"JSON validation failed: {e.message}, {list(e.path)}")	
 
 
	