"""API test Delete user"""


import pytest
import requests
from tests.api.test_data_api_users import BASE_URL


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_delete_user(auth_token_and_user_data):
    """Positive test: Successfully delete a user."""
    token, _ = auth_token_and_user_data  # Распаковываем кортеж
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.delete(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    assert response.text == "", ("Expected empty response body "
                                 "for successful delete")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_delete_user_invalid_token():
    """Negative test: Attempt to delete a user with an invalid token."""
    invalid_token = "invalid_token"
    headers = {
        "Authorization": f"Bearer {invalid_token}"
    }

    response = requests.delete(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
    response_data = response.json()
    assert response_data.get("error") == "Please authenticate.", \
        (f"Expected error message 'Please authenticate.', "
         f"but got {response_data.get('error')}")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_delete_user_twice(auth_token_and_user_data):
    """Negative test: Attempt to delete a user twice."""
    token, _ = auth_token_and_user_data  # Распаковываем кортеж
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response1 = requests.delete(f"{BASE_URL}/users/me", headers=headers)
    assert response1.status_code == 200, (f"Expected status 200, "
                                          f"but got {response1.status_code}")
    assert response1.text == "", ("Expected empty response body "
                                  "for successful delete")

    response2 = requests.delete(f"{BASE_URL}/users/me", headers=headers)
    assert response2.status_code == 401, (f"Expected status 401, "
                                          f"but got {response2.status_code}")
    response_data = response2.json()
    assert response_data.get("error") == "Please authenticate.", \
        (f"Expected error message 'Please authenticate.', "
         f"but got {response_data.get('error')}")


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_delete_user_non_existent(auth_token_and_user_data):
    """Negative test: Attempt to delete a non-existent user."""
    invalid_token = "invalid_token"
    headers = {
        "Authorization": f"Bearer {invalid_token}"
    }

    response = requests.delete(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
    assert response.text == '{"error":"Please authenticate."}', \
        "Expected error message for unauthorized access"
