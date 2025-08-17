import os
import pytest
import requests
from util import file_util
from util.email_util import send_email

# Get an authentication token for API requests, obsolete, use token.get() instead
@pytest.fixture(scope='session')
def get_auth_token():
    url="https://qv77wuaaytru4gzchjj7bhewhq0ukysc.lambda-url.us-west-2.on.aws/auth"
    payload = {"apiKey": "test-key-001"}
    response = requests.post(url, json=payload)
    response.raise_for_status()
    if response.status_code == 200:
        return response.json().get("token")
    #todo handle expired token


# Global variable to store report path (shared between fixture and hook function)
REPORT_PATH = os.path.join("doc", "report", "html", "test_report.html")

@pytest.fixture(scope='session', autouse=True)
def manage_report():
    # Clean report directory before tests
    report_dir = os.path.join("doc", "report")
    file_util.clean_directory(report_dir)
    yield  # Test execution phase

@pytest.hookimpl(trylast=True)  # Ensure this hook runs after all report generation
def pytest_sessionfinish(session):
    # Condition 1: Ensure report file exists and is not empty
    if not (os.path.exists(REPORT_PATH) and os.path.getsize(REPORT_PATH) > 0):
        print(f"Skipping email: Report file does not exist or is empty ({REPORT_PATH})")
        return

    # Condition 2: Check if any test cases were actually executed
    test_counts = session.testscollected
    if test_counts == 0:
        print("Skipping email: No test cases were executed")
        return
    
    # Send email after entire test session completes (report is generated)
    if os.path.exists(REPORT_PATH):
        sender_email = 'zhhot@sohu.com'
        sender_password =  os.getenv("EMAIL_PASSWORD") 
        receiver_email = 'zhhot@hotmail.com'
        subject = 'Pytest Test Report'
        body = 'Please find the attached Pytest test report.'
        send_email(sender_email, sender_password, receiver_email, subject, body, REPORT_PATH)
    else:
        print(f"Warning: Test report file not found at {REPORT_PATH}")











