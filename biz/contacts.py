
import requests
import pytest
from util import json_util


TIMEOUT=10
CONTACTS_URL = "https://qv77wuaaytru4gzchjj7bhewhq0ukysc.lambda-url.us-west-2.on.aws/contacts"

# Get contacts from the API using the provided token
def get(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(CONTACTS_URL, headers=headers, timeout=TIMEOUT)
    
    return response

# Validate the JSON structure against the schema
def validate_schema(contacts):
    schema = json_util.load_schema("data/schema/contacts_schema.json")
    
    return json_util.validate_json(contacts, schema)

# Validate the JSON structure against the invalid schema
def validate_invalid_schema(contacts):
    schema = json_util.load_schema("data/schema/contacts_schema_invalid.json")
    
    return json_util.validate_json(contacts, schema)