"""API tests Add user"""


import requests
import pytest
from tests.test_data.data_api_users import BASE_URL, HEADERS, UserData


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_add_user_success():
    """Positive tests: successful user registration."""
    user_data = UserData.generate_user_data()

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 201, (f"Expected status 201, "
                                         f"but got {response.status_code}")

    response_data = response.json()

    assert "token" in response_data, "Expected 'token' in the response data"
    assert "user" in response_data, "Expected 'user' in the response data"


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_add_user_existing_email():
    """Negative tests: adding a user with an existing email."""
    user_data = UserData.generate_user_data()

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 201, (f"Expected status 201, "
                                         f"but got {response.status_code}")

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    assert "error" in response_data or "message" in response_data, \
        "Expected an error message in the response"


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_add_user_no_first_name():
    """Negative tests: adding a user without the required 'firstName' field."""
    user_data = UserData.generate_user_data()
    del user_data["firstName"]

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    assert "error" in response_data or "message" in response_data, \
        "Expected an error message in the response"
    assert "firstname" in response_data.get("message", "").lower(), \
        "Expected error related to 'firstName'"


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_add_user_invalid_email():
    """Negative tests: adding a user with an invalid email format."""
    user_data = UserData.generate_user_data()
    user_data["email"] = "invalid-email-format"

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    assert "error" in response_data or "message" in response_data, \
        "Expected an error message in the response"
    assert "email" in response_data.get("message", "").lower(), \
        "Expected error related to 'email'"


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_add_user_short_password():
    """Negative tests: adding a user with a short password."""
    user_data = UserData.generate_user_data()
    user_data["password"] = "short"

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    assert "error" in response_data or "message" in response_data, \
        "Expected an error message in the response"
    assert "password" in response_data.get("message", "").lower(), \
        "Expected error related to 'password'"
