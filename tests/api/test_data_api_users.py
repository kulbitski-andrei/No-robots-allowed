import uuid

BASE_URL = "https://thinking-tester-contact-list.herokuapp.com"

HEADERS = {
    "Content-Type": "application/json"
}


class UserData:
    """Class for random user data generation"""
    @staticmethod
    def generate_user_data():
        """Generate user data for registration."""
        return {
            "email": f"user_{uuid.uuid4()}@example.com",
            "firstName": "Test",
            "lastName": "User",
            "password": "ValidPassword123"
        }

    @staticmethod
    def generate_non_existent_email():
        """Generate an email that is guaranteed not to exist."""
        return f"nonexistent_{uuid.uuid4()}@example.com"
