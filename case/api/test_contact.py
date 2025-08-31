import pytest
from datetime import datetime
from util.log_util import log
import biz.api


@log.log_method()
@pytest.mark.security
@pytest.mark.api
@pytest.mark.parametrize("expected_status,token", 
    [
        # 0. Valid token test
        (200, biz.api.token.get()),    
        
        # 1. Null/missing value tests
        (401, ""),
        (401, " "),
        (401, None),
  
        # 2. Special character tests
        (401, "!@#$%^&*()`~-_=+[]{}|\\;:'\",.<>?/"),
        (401, ''.join(chr(c) for c in range(128, 192))), #  latin_1 special symbols  (401, "€†‡ˆ‰‹Œ‘’“”•–—˜™›œ£¥©®")
        (401,''.join(chr(c) for c in range(192,256))),  # latin_1 accented characters (401, "ñáéíóú")
        # (401, "中文双字节字符"),  #Invalid use case # Todo: UnicodeEncodeError: 'latin-1' codec can't encode characters in position 18-24: ordinal not in range(256)

        # 3. Data type tests
        (401, True),
        (401, 12345),
        (401, datetime.now()),
  
        # 4. Length boundary tests
        (401, "a" * 1),  
        (413, "a" * 10893),     # 413 Payload Too Large, means request body is too large. Should be 431 Request Header Fields Too Large.
        (400, "a" * (2**16+1)), # The maximum length of the http header：8KB–64KB. Should be 431 Request Header Fields Too Large.
    
        # 5. Security attack tests
        (401, "<script>alert('XSS')</script>"), 
        (401, "' OR '1'='1"),    
        (401, "{{7*7}}"),
  
        # 6. Expired token tests
        (401, "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmaXJzdE5hbWUiOiJKb2huIiwibGFzdE5hbWUiOiJEb2UiLCJyb2xlIjoiUUEgQ2FuZGlkYXRlIiwiaWF0IjoxNzU1MjAxMjkxLCJleHAiOjE3NTUyODc2OTF9.f0Bs4FW2AAbniCQMtnWsjwN1_MlUYyLM2koZdfngDfc"),
      ],
    ids=[
        # 0. Valid token test
        "valid_token",
        
        # 1. Null/missing value tests
        "empty_token",
        "whitespace_token",
        "none_token",

        # 2. Special character tests
        "special_symbols_token",
        "latin_special_symbols_token",
        "latin_accented_characters_token",
        # "chinese_doublebyte_token",

        # 3. Data type tests
        "boolean_token",
        "numeric_token",
        "datetime_object_token",

        # 4. Length boundary tests
        "min_length_token",
        "long_token",
        "extra_long_token",

        # 5. Security attack tests
        "xss_injection_token",
        "sql_injection_token",
        "template_injection_token",

        # 6. Expired token tests
        "expired_jwt_token"
    ]            
)
def test_get_contacts(expected_status,token):  
    log.logger.info("Step 1: Make the GET request to fetch contacts")
    response = biz.api.contact.get(token)
 
    log.logger.info("Step 2: Validate the response status code")
    assert response.status_code == expected_status
    
    log.logger.info("Step 3: Validate the JSON structure against the schema")
    assert biz.api.contact.validate_response(response)
   

@pytest.mark.api
@pytest.mark.stress
def test_get_contacts_batch():
    for i in range(1, 10, 1): # range(2**13, 2**16, 2**10) #range(10893, 10992,1) 
        token= "a" * i
        response = biz.contacts.get(token)
        log.logger.info("status_code=%s, token_length=%d", response.status_code, len(token))


@log.log_method()
@pytest.mark.security
@pytest.mark.api
@pytest.mark.parametrize("expected_status,id", 
    [
        # 0. Valid & Invalid user id
        (200, "test-123"),
        (404, "test-1"), #  disable or deleted user id
        
        # 1. Null/missing value tests
        (404, ""),
        (404, " "),
        (404, None),
          
        # 2. Special character tests
        (404, "!@#$%^&*()`~-_=+[]{}|\\;:'\",.<>?/"),
        (404, ''.join(chr(c) for c in range(128, 256))), #  latin_1 special symbols  (401, "€†‡ˆ‰‹Œ‘’“”•–—˜™›œ£¥©®")
        (404,"中文双字节字符"), 

        # 3. Data type tests
        (404, True),
        (404, 12345),
        (404, datetime.now()),
  
        # 4. Length boundary tests
        (404, "a" * 1),  
        (404, "a" * 10893),     
        (414, "a" * (2**16+1)), #Request-URI Too Long
    
        # 5. Security attack tests
        (404, "<script>alert('XSS')</script>"), 
        (404, "' OR '1'='1"),    
        (404, "{{7*7}}"),
    ],
    ids=[
        # 0. Valid & Invalid test
        "valid_user",
        "Invalid_user", 
        
        # 1. Null/missing value tests
        "empty",
        "whitespace",
        "none",
        
        # 2. Special character tests
        "special_symbols",
        "latin_special_symbols",
        "chinese_doublebyte",

        # 3. Data type tests
        "boolean",
        "numeric",
        "datetime_object",

        # 4. Length boundary tests
        "min_length",
        "long",
        "extra_long",

        # 5. Security attack tests
        "xss_injection",
        "sql_injection",
        "template_injection",
    ]
)
def test_get_contact(expected_status,id):
    log.logger.info("Step 1: Get the authentication token")
    token= biz.api.token.get()
    
    log.logger.info("Step 2: Make the GET request to fetch contacts")
    response = biz.api.contact.get(token,id)
 
    log.logger.info("Step 3: Validate the response status code")
    assert response.status_code == expected_status
    
    log.logger.info("Step 4: Validate the JSON structure against the schema")
    assert biz.api.contact.validate_response(response)
    


@log.log_method()
@pytest.mark.api
def test_sample ():
    log.logger.info("Step 1")
    log.logger.info("Step 2")
    
    pass


