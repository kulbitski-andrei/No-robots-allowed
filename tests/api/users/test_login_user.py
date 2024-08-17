import pytest
import requests
from tests.api.test_data_api_users import BASE_URL, HEADERS, UserData


@pytest.fixture
def auth_token_and_user_data():
    """Fixture to authenticate, retrieve a token, and user data."""
    # Generate user data using UserData
    user_data = UserData.generate_user_data()

    response = requests.post(f"{BASE_URL}/users", json=user_data, headers=HEADERS)
    assert response.status_code == 201, f"Expected status 201, but got {response.status_code}"

    response_data = response.json()
    token = response_data.get("token")

    assert token is not None, "Expected 'token' in the response data"

    return token, user_data


def test_login_user_success(auth_token_and_user_data):
    """Positive test: Log in with correct credentials."""
    token, user_data = auth_token_and_user_data
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }

    response = requests.post(f"{BASE_URL}/users/login", json=login_data, headers=HEADERS)

    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
    response_data = response.json()

    assert "token" in response_data, "Expected 'token' in the response data"
    assert response_data["token"] is not None, "Expected 'token' to be not None"


def test_login_user_incorrect_password(auth_token_and_user_data):
    """Negative test: Attempt to log in with incorrect password."""
    token, user_data = auth_token_and_user_data
    login_data = {
        "email": user_data["email"],
        "password": "IncorrectPassword"
    }

    response = requests.post(f"{BASE_URL}/users/login", json=login_data, headers=HEADERS)

    assert response.status_code == 401, f"Expected status 401, but got {response.status_code}"

    if response.text:
        try:
            response_data = response.json()
            assert "error" in response_data, "Expected 'error' in the response data"
            assert response_data["error"] == "Invalid email or password", "Expected error message for incorrect password"
        except ValueError:
            assert response.text == "", "Expected empty response body for incorrect password"
    else:
        assert response.text == "", "Expected empty response body for incorrect password"


def test_login_user_non_existent_email():
    """Negative test: Attempt to log in with a non-existent email."""
    login_data = {
        "email": UserData.generate_non_existent_email(),  # Use a method to generate a non-existent email
        "password": "ValidPassword123"
    }

    response = requests.post(f"{BASE_URL}/users/login", json=login_data, headers=HEADERS)

    assert response.status_code == 401, f"Expected status 401, but got {response.status_code}"
    assert response.text == "", "Expected empty response body for non-existent email"


def test_login_user_invalid_email_format():
    """Negative test: Attempt to log in with an invalid email format."""
    login_data = {
        "email": "invalid-email-format",
        "password": "ValidPassword123"
    }

    response = requests.post(f"{BASE_URL}/users/login", json=login_data, headers=HEADERS)

    assert response.status_code == 401, f"Expected status 401, but got {response.status_code}"
    assert response.text == "", "Expected empty response body for invalid email format"
