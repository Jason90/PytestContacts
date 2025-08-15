from datetime import datetime
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
 

@pytest.mark.security
@pytest.mark.api
@pytest.mark.parametrize("expected_status,token", 
	[
		#1. Null/missing value tests
  		(401, ""),
        (401, " "),
        (401, None),
  
        # 2. Special character tests
        (401, "!@#$%^&*()[]\\{}|;':\"\",./<>?"),
        (401, "ñáéíóú"),
        (401, "中文双字节字符"),  # # Todo: UnicodeEncodeError: 'latin-1' codec can't encode characters in position 18-24: ordinal not in range(256)

    
        # 3. Data type tests
        (401, True),
        (401, 12345),
        (401, datetime.now()),
  
        # 4. Length boundary tests
        (401, "a" * 1),  
        (401, "a" * (2**13)), 
        (400, "a" * (2**16)),  # Todo: Whether the 400 error is reasonable needs to be confirmed. The maximum length of the http header

    
        # 5. Security attack tests
        (401, "<script>alert('XSS')</script>"),
        (401, "' OR '1'='1"),	
        (401, "{{7*7}}"),
  
        # 6. Expired token tests
        (401, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaXJzdE5hbWUiOiJKb2huIiwibGFzdE5hbWUiOiJEb2UiLCJyb2xlIjoiUUEgQ2FuZGlkYXRlIiwiaWF0IjoxNzU1MjAxMjkxLCJleHAiOjE3NTUyODc2OTF9.f0Bs4FW2AAbniCQMtnWsjwN1_MlUYyLM2koZdfngDfc"),
  	],
    ids=[
        # 1. Null/missing value tests
        "empty_token",
        "whitespace_token",
        "none_token",

        # 2. Special character tests
        "special_symbols_token",
        "unicode_latin_extended_token",
        "chinese_doublebyte_token",

        # 3. Data type tests
        "boolean_token",
        "numeric_token",
        "datetime_object_token",

        # 4. Length boundary tests
        "min_length_token(1_char)",
        "long_token(2^13_chars)",
        "extra_long_token(2^16_chars)",

        # 5. Security attack tests
        "xss_injection_token",
        "sql_injection_token",
        "template_injection_token",

        # 6. Expired token tests
        "expired_jwt_token"
    ]			
)
def test_get_contacts_with_invalid_token(expected_status,token):
	# Step 1: Make the GET request to fetch contacts
	contacts = biz.contacts.get(token)
 
	# Step 2: Validate the response status code
	assert contacts.status_code == expected_status
 
	# Step 3: Validate the JSON structure against the schema
	data= contacts.json()
	if expected_status == 200:
		assert biz.contacts.validate_schema(data)
	else:
		assert biz.contacts.validate_invalid_schema(data)
	