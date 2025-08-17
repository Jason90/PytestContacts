
import requests
import pytest
from util import json_util
from config import CONTACTS_URL, TIMEOUT


# Get contacts from the API using the provided token.
def get(token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = requests.get(CONTACTS_URL, headers=headers, timeout=TIMEOUT)
    
    return response

# Validate the JSON structure against the schema
def validate_schema(contacts):
    schema = json_util.load_schema("contacts_schema.json")
    
    return json_util.validate_json(contacts, schema)

# Validate the JSON structure against the invalid schema
def validate_invalid_schema(contacts):
    schema = json_util.load_schema("contacts_schema_invalid.json")
    
    return json_util.validate_json(contacts, schema)