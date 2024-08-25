"""API test Logout user"""


import pytest
import requests
from test.api.test_data_api_users import BASE_URL


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_logout_user(auth_token_and_user_data):
    """Positive test: Successfully log out a user."""
    token, _ = auth_token_and_user_data  # распаковываем кортеж
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.post(f"{BASE_URL}/users/logout",
                             headers=headers)

    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    assert response.text == "", ("Expected empty response body "
                                 "for successful logout")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
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


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_logout_user_twice(auth_token_and_user_data):
    """Negative test: Attempt to log out twice."""
    token, _ = auth_token_and_user_data
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
