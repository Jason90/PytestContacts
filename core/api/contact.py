
from util import http_util, json_util
from config import API_Config
from util.log_util import log

# Get contact/contacts from the API using the provided token.
def get(token,id=None):
    url = f"{API_Config.API_CONTACTS_URL}/{id}" if id is not None else API_Config.API_CONTACTS_URL
    
    response = http_util.get(url, headers=http_util.generate_header(token), timeout=API_Config.HTTP_TIMEOUT)
    
    return response

# Validate the JSON structure against the schema
def validate_response(response) -> bool:
    contentType = response.headers.get("Content-Type", "")
    if("application/json" in contentType):
        if "/" in response.url.replace(API_Config.API_BASE_URL, "", 1):
            api="contact"
        else:
            api="contacts"
        schema_file_name=f"{api}_{response.request.method}_{response.status_code}.json"    
        log.logger.info(f"Schema file name {schema_file_name}")
        schema = json_util.load_schema(schema_file_name)
    
        return json_util.validate_json(response.json(), schema)
    else:
        log.logger.warning("Response is not in JSON format. status_code=%s, contentType=%s",response.status_code,contentType)
        log.logger.debug("Response text:", response.text)
        
        return True