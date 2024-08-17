"""API test Get user info"""


import requests
import pytest
from tests.api.test_data_api_users import BASE_URL, HEADERS, UserData


@pytest.fixture(scope="session")
def auth_token_and_user_data():
    """Fixture to authenticate, retrieve a token, and user data."""
    # Generate user data with a unique email
    user_data = UserData.generate_user_data()

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 201, (f"Expected status 201, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    token = response_data["token"]

    return token, user_data


def test_get_user_profile(auth_token_and_user_data):
    """Test to get the user's profile information."""
    auth_token, user_data = auth_token_and_user_data
    headers = {
        "Authorization": f"Bearer {auth_token}",
        **HEADERS  # Merge with default headers
    }

    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")

    profile_data = response.json()

    # Check that the profile data contains the expected keys
    assert "email" in profile_data, \
        "Expected 'email' in the profile data"
    assert "firstName" in profile_data, \
        "Expected 'firstName' in the profile data"
    assert "lastName" in profile_data, \
        "Expected 'lastName' in the profile data"
    assert "_id" in profile_data, \
        "Expected '_id' in the profile data"

    # Verify that the email in the profile matches
    # what was used for registration
    assert profile_data["email"] == user_data["email"], \
        ("The email in the profile "
         "does not match the registered email")


def test_get_user_profile_invalid_token():
    """Negative test: Retrieve user profile with an invalid token."""
    invalid_token = "invalidtoken"
    headers = {
        "Authorization": f"Bearer {invalid_token}",
        **HEADERS  # Merge with default headers
    }

    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
    response_data = response.json()

    # Check that the error message is as expected
    assert "error" in response_data, "Expected 'error' in the response data"
    assert response_data["error"] == "Please authenticate.", \
        "Expected 'Please authenticate.' message"
