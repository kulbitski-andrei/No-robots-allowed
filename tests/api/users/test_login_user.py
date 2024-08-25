"""API tests Login user"""


import pytest
import requests
from test_data.data_api_users import BASE_URL, HEADERS, UserData


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_login_user_success(auth_token_and_user_data):
    """Positive tests: Log in with correct credentials."""
    token, user_data = auth_token_and_user_data
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }

    response = requests.post(f"{BASE_URL}/users/login",
                             json=login_data, headers=HEADERS)

    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_data = response.json()

    assert "token" in response_data, \
        "Expected 'token' in the response data"
    assert response_data["token"] is not None, \
        "Expected 'token' to be not None"


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_login_user_incorrect_password(auth_token_and_user_data):
    """Negative tests: Attempt to log in with incorrect password."""
    token, user_data = auth_token_and_user_data
    login_data = {
        "email": user_data["email"],
        "password": "IncorrectPassword"
    }

    response = requests.post(f"{BASE_URL}/users/login",
                             json=login_data, headers=HEADERS)

    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")

    if response.text:
        try:
            response_data = response.json()
            assert "error" in response_data, ("Expected 'error' "
                                              "in the response data")
            assert response_data["error"] == "Invalid email or password", \
                "Expected error message for incorrect password"
        except ValueError:
            assert response.text == "", ("Expected empty response body "
                                         "for incorrect password")
    else:
        assert response.text == "", ("Expected empty response body "
                                     "for incorrect password")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_login_user_non_existent_email():
    """Negative tests: Attempt to log in with a non-existent email."""
    login_data = {
        "email": UserData.generate_non_existent_email(),
        "password": "ValidPassword123"
    }

    response = requests.post(f"{BASE_URL}/users/login",
                             json=login_data, headers=HEADERS)

    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
    assert response.text == "", ("Expected empty response body "
                                 "for non-existent email")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_login_user_invalid_email_format():
    """Negative tests: Attempt to log in with an invalid email format."""
    login_data = {
        "email": "invalid-email-format",
        "password": "ValidPassword123"
    }

    response = requests.post(f"{BASE_URL}/users/login",
                             json=login_data, headers=HEADERS)

    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
    assert response.text == "", ("Expected empty response body "
                                 "for invalid email format")
