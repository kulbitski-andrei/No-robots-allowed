"""API test Get user info"""


import requests
import pytest
from tests.api.test_data_api_users import BASE_URL, HEADERS, UserData


@pytest.mark.priority_high
@pytest.mark.api_getuser
@pytest.mark.level_smoke
def test_get_user_profile(auth_token_and_user_data):
    """Test to get the user's profile information."""
    auth_token, user_data = auth_token_and_user_data
    headers = {
        "Authorization": f"Bearer {auth_token}",
        **HEADERS
    }

    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")

    profile_data = response.json()

    assert "email" in profile_data, \
        "Expected 'email' in the profile data"
    assert "firstName" in profile_data, \
        "Expected 'firstName' in the profile data"
    assert "lastName" in profile_data, \
        "Expected 'lastName' in the profile data"
    assert "_id" in profile_data, \
        "Expected '_id' in the profile data"

    assert profile_data["email"] == user_data["email"], \
        ("The email in the profile "
         "does not match the registered email")


@pytest.mark.priority_medium
@pytest.mark.api_getuser
@pytest.mark.level_regression
def test_get_user_profile_invalid_token():
    """Negative test: Retrieve user profile with an invalid token."""
    invalid_token = "invalidtoken"
    headers = {
        "Authorization": f"Bearer {invalid_token}",
        **HEADERS
    }

    response = requests.get(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
    response_data = response.json()

    assert "error" in response_data, "Expected 'error' in the response data"
    assert response_data["error"] == "Please authenticate.", \
        "Expected 'Please authenticate.' message"
