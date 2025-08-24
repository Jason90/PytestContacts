from datetime import datetime, timedelta
from config import TOKEN_URL, HTTP_TIMEOUT, PAYLOAD
from util import http_util
from util.log_util import LoggerFactory

log = LoggerFactory.get_log_aspect()

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
        
        new_token_data = _get_new()
        _token_cache["token"] = new_token_data["token"]
        _token_cache["expires_at"] = new_token_data["expires_at"]
        log.logger.info("New token obtained, will expire at %s", _token_cache["expires_at"])
    
    return _token_cache["token"]

# Get new token from the API
def _get_new():
    response = http_util.post(TOKEN_URL, data=PAYLOAD, timeout=HTTP_TIMEOUT)
    
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
    return "Invalid token"