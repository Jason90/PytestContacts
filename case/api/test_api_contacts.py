import biz.token
import biz.contacts
import pytest


@pytest.mark.smoke
@pytest.mark.api
def test_get_contacts():
    # Step 1: Get the authentication token
	token= biz.token.get()
 
	# Step 2: Make the GET request to fetch contacts
	contacts=biz.contacts.get(token)
 
	# Step 3: Validate the response status code
	assert contacts.status_code == 200
 
	# Step 4: Validate the JSON structure against the schema
	assert biz.contacts.validate_schema(contacts.json())
 
@pytest.mark.smoke
@pytest.mark.api
def test_get_contacts_invalid_token():
    # Step 1: Get the authentication token
	token= biz.token.get_invalid()
	
	# Step 2: Make the GET request to fetch contacts
	contacts=biz.contacts.get(token)
 
	# Step 3: Validate the response status code
	assert contacts.status_code == 401
	
	# Step 4: Validate the JSON structure against the schema
	assert biz.contacts.validate_invalid_schema(contacts.json())
 