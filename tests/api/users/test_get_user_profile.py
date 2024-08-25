"""API tests Get user info"""


import requests
import pytest
from tests.test_data.data_api_users import BASE_URL, HEADERS


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
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
