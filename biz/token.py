import pytest
import requests
from datetime import datetime, timedelta


TIMEOUT=10
TOKEN_URL="https://qv77wuaaytru4gzchjj7bhewhq0ukysc.lambda-url.us-west-2.on.aws/auth" #todo url and payload should be in a config file

# Authentication payload
PAYLOAD = {"apiKey": "test-key-001"}

# Cache for the token to avoid frequent requests
_token_cache = {
    "token": None,
    "expires_at": None
}
    
# Get cached token to avoid frequent requests
def get():
    global _token_cache
    now = datetime.now()
    if (_token_cache is None or _token_cache["token"] is None or 
        _token_cache["expires_at"] is None or 
        now >= _token_cache["expires_at"] - timedelta(seconds=60)):
        
        # 
        new_token_data = get_new()
        _token_cache["token"] = new_token_data["token"]
        _token_cache["expires_at"] = new_token_data["expires_at"]
        print(f"New token obtained, will expire at {_token_cache['expires_at']}")
    
    return _token_cache["token"]

# Get new token from the API
def get_new():
    response = requests.post(TOKEN_URL, json=PAYLOAD)
    
    response.raise_for_status()
    auth_data = response.json()
    
    # Check if the response contains the token and expiration time   
    expires_in = auth_data.get("expiresIn", 3600)  
    expires_at = datetime.now() + timedelta(seconds=expires_in)
    
    return {
        "token": auth_data["token"],
        "expires_at": expires_at
    }

# Get an invalid token for testing purposes
def get_invalid():
    return {"token": "Invalid token"}