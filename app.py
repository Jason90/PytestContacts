import logging
import requests
from util.log_util import LoggerFactory
from util.email_util import send_email


# 1. Initialize logging configuration (once globally)
def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )


# 2. Get log aspect
log_aspect = LoggerFactory.get_log_aspect("api_tests")
log_method = log_aspect.log_method


# 3. Business logic (decoupled from logging implementation)
class ApiService:
    @log_method(description="Get user information")  # Apply log aspect
    def get_user(self, user_id: int):
        url = f"https://api.example.com/users/{user_id}"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    
    @log_method(description="Create new user")
    def create_user(self, name: str, email: str):
        url = "https://api.example.com/users"
        data = {"name": name, "email": email}
        response = requests.post(url, json=data, timeout=10)
        response.raise_for_status()
        return response.json()


# 4. Test cases
def test_api_service():
    setup_logging()
    service = ApiService()
    
    # Call methods with log aspect
    try:
        user = service.get_user(123)
        print(f"Fetched user: {user}")
        
        new_user = service.create_user("Test User", "test.user@example.com")
        print(f"Created user: {new_user}")
    except Exception as e:
        print(f"Operation failed: {e}")


# if __name__ == "__main__":
#     test_api_service()
    