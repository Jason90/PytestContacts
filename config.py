
class API_Config:
    HTTP_TIMEOUT=10
    PAYLOAD = {"apiKey": "test-key-001"}
    API_BASE_URL="https://qv77wuaaytru4gzchjj7bhewhq0ukysc.lambda-url.us-west-2.on.aws/" # API_BASE_URL="https://qv77wuaaytru4gzchjj7bhewhq0ukysc.lambda-url.us-west-2.on.aws/prod/" 
    API_TOKEN_URL = f"{API_BASE_URL}auth"
    API_CONTACTS_URL = f"{API_BASE_URL}contacts"


class Web_Config:
    WEB_BASE_URL="https://www.everbridge.com/"
    WEB_LOGIN_URL="https://authentication.everbridge.net/cas/login"


class Report_Config:
    EMAIL_SMTP_SERVER='smtp.sohu.com'
    SEND_REPORT = False