"""API test Logout user"""


import pytest
import requests
from tests.api.test_data_api_users import BASE_URL, HEADERS, UserData


@pytest.mark.priority_high
@pytest.mark.api_logout
@pytest.mark.level_smoke
def test_logout_user(auth_token_and_user_data):
    """Positive test: Successfully log out a user."""
    token = auth_token_and_user_data["token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(f"{BASE_URL}/users/logout",
                             headers=headers)

    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    assert response.text == "", ("Expected empty response body "
                                 "for successful logout")


@pytest.mark.priority_medium
@pytest.mark.api_logout
@pytest.mark.level_regression
def test_logout_user_invalid_token():
    """Negative test: Attempt to log out with an invalid token."""
    invalid_token = "invalid_token"
    headers = {
        "Authorization": f"Bearer {invalid_token}"
    }

    response = requests.post(f"{BASE_URL}/users/logout", headers=headers)

    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
    response_data = response.json()
    assert response_data.get("error") == "Please authenticate.", \
        (f"Expected error message 'Please authenticate.', "
         f"but got {response_data.get('error')}")


@pytest.mark.priority_medium
@pytest.mark.api_logout
@pytest.mark.level_regression
def test_logout_user_twice(auth_token_and_user_data):
    """Negative test: Attempt to log out twice."""
    token = auth_token_and_user_data["token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response1 = requests.post(f"{BASE_URL}/users/logout", headers=headers)
    assert response1.status_code == 200, (f"Expected status 200, "
                                          f"but got {response1.status_code}")
    assert response1.text == "", ("Expected empty response body "
                                  "for successful logout")

    response2 = requests.post(f"{BASE_URL}/users/logout",
                              headers=headers)
    assert response2.status_code == 401, (f"Expected status 401, "
                                          f"but got {response2.status_code}")
    response_data = response2.json()
    assert response_data.get("error") == "Please authenticate.", \
        (f"Expected error message 'Please authenticate.', "
         f"but got {response_data.get('error')}")
