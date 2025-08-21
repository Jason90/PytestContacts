import os
import pytest
from util import file_util
from util.email_util import send_email
import logging

logger = logging.getLogger(__name__)

# Global variable to store report path (shared between fixture and hook function)
REPORT_PATH = os.path.join("doc", "report", "html", "test_report.html")

@pytest.fixture(scope='session', autouse=True)
def manage_report():
    logger.info("Setting up report directory, cleaning if necessary")
    report_dir = os.path.join("doc", "report")
    file_util.clean_directory(report_dir)
    
    yield  # This will run after all tests complete
    
    # If you want to send the email after all tests are done, don't do it here. 
    # Report generation and email sending should be handled in a hook.

@pytest.hookimpl(trylast=True) 
def pytest_sessionfinish(session):
    logger.info("Session finished, preparing to send email with report")
    # Condition 1: Ensure report file exists and is not empty
    if not (os.path.exists(REPORT_PATH) and os.path.getsize(REPORT_PATH) > 0):
        logger.warning(f"Skipping email: Report file does not exist or is empty: {REPORT_PATH}")
        return

    # Condition 2: Check if any test cases were actually executed
    test_counts = session.testscollected
    if test_counts == 0:
        logger.warning("Skipping email: No test cases were executed")
        return
    
    # Send email after entire test session completes (report is generated)
    sender_email = 'zhhot@sohu.com'
    sender_password =  os.getenv("EMAIL_PASSWORD") 
    receiver_email = 'zhhot@hotmail.com'
    subject = 'Pytest Test Report'
    body = 'Please find the attached Pytest test report.'
    send_email(sender_email, sender_password, receiver_email, subject, body, REPORT_PATH)












