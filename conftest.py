import os
import pytest
from util import file_util
from util.email_util import send_email
from util.log_util import log
from config import Report_Config

# Global variable to store report path (shared between fixture and hook function)
REPORT_PATH = os.path.join("doc", "report", "html", "test_report.html")

@pytest.fixture(scope='session', autouse=True)
def manage_report():
    log.logger.info("Setting up report directory, cleaning if necessary")
    report_dir = os.path.join("doc", "report")
    # file_util.clean_directory(report_dir)
    
    yield  # This will run after all tests complete
    
    # If you want to send the email after all tests are done, don't do it here. 
    # Report generation and email sending should be handled in a hook.

@pytest.hookimpl(trylast=True) 
def pytest_sessionfinish(session):
    # Condition 1: Check if email sending is enabled via configuration
    if not Report_Config.SEND_REPORT:
        log.logger.warning("Email sending is disabled via configuration")
        return
    
    # Condition 2: Ensure report file exists and is not empty
    if not (os.path.exists(REPORT_PATH) and os.path.getsize(REPORT_PATH) > 0):
        log.logger.warning(f"Skipping email: Report file does not exist or is empty: {REPORT_PATH}")
        return

    # Condition 3: Check if any test cases were actually executed
    test_counts = session.testscollected
    if test_counts == 0:
        log.logger.warning("Skipping email: No test cases were executed")
        return
    
    # Send email after entire test session completes (report is generated)
    log.logger.info("Session finished, preparing to send email with report")
    sender_email = 'zhhot@sohu.com'
    sender_password =  os.getenv("EMAIL_PASSWORD") 
    receiver_email = 'zhhot@hotmail.com'
    subject = 'Pytest Test Report'
    body = 'Please find the attached Pytest test report.'
    send_email(sender_email, sender_password, receiver_email, subject, body, REPORT_PATH)


# def pytest_addoption(parser):
#     parser.addini("send_report", "Send report after tests", default="false")




