"""API test Add user"""


import requests
from tests.api.test_data_api_users import BASE_URL, HEADERS, UserData


def test_add_user_success():
    """Positive test: successful user registration."""
    user_data = UserData.generate_user_data()

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 201, (f"Expected status 201, "
                                         f"but got {response.status_code}")

    response_data = response.json()

    assert "token" in response_data, "Expected 'token' in the response data"
    assert "user" in response_data, "Expected 'user' in the response data"


def test_add_user_existing_email():
    """Negative test: adding a user with an existing email."""
    # First, create a user with a unique email
    user_data = UserData.generate_user_data()

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 201, (f"Expected status 201, "
                                         f"but got {response.status_code}")

    # Try to create another user with the same email
    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    assert "error" in response_data or "message" in response_data, \
        "Expected an error message in the response"


def test_add_user_no_first_name():
    """Negative test: adding a user without the required 'firstName' field."""
    user_data = UserData.generate_user_data()
    del user_data["firstName"]  # Remove the required 'firstName' field

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    assert "error" in response_data or "message" in response_data, \
        "Expected an error message in the response"
    assert "firstname" in response_data.get("message", "").lower(), \
        "Expected error related to 'firstName'"


def test_add_user_invalid_email():
    """Negative test: adding a user with an invalid email format."""
    user_data = UserData.generate_user_data()
    user_data["email"] = "invalid-email-format"  # Set an invalid email

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    assert "error" in response_data or "message" in response_data, \
        "Expected an error message in the response"
    assert "email" in response_data.get("message", "").lower(), \
        "Expected error related to 'email'"


def test_add_user_short_password():
    """Negative test: adding a user with a short password."""
    user_data = UserData.generate_user_data()
    user_data["password"] = "short"  # Set a password that is too short

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    assert "error" in response_data or "message" in response_data, \
        "Expected an error message in the response"
    assert "password" in response_data.get("message", "").lower(), \
        "Expected error related to 'password'"
