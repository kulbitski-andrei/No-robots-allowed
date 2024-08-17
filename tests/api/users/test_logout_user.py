"""API test Logout user"""


import pytest
import requests
from tests.api.test_data_api_users import BASE_URL, HEADERS, UserData


@pytest.fixture
def auth_token_and_user_data():
    """Fixture to create a registered user and obtain an auth token."""
    user_data = UserData.generate_user_data()

    # Регистрация пользователя
    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 201, (f"Expected status 201, "
                                         f"but got {response.status_code}")

    # Логин пользователя
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_response = requests.post(f"{BASE_URL}/users/login",
                                   json=login_data, headers=HEADERS)
    assert login_response.status_code == 200, \
        f"Expected status 200, but got {login_response.status_code}"

    response_data = login_response.json()
    return {
        "email": user_data["email"],
        "password": user_data["password"],
        "token": response_data["token"]
    }


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


def test_logout_user_twice(auth_token_and_user_data):
    """Negative test: Attempt to log out twice."""
    token = auth_token_and_user_data["token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Первый выход
    response1 = requests.post(f"{BASE_URL}/users/logout", headers=headers)
    assert response1.status_code == 200, (f"Expected status 200, "
                                          f"but got {response1.status_code}")
    assert response1.text == "", ("Expected empty response body "
                                  "for successful logout")

    # Попытка выхода снова с тем же токеном
    response2 = requests.post(f"{BASE_URL}/users/logout",
                              headers=headers)
    assert response2.status_code == 401, (f"Expected status 401, "
                                          f"but got {response2.status_code}")
    response_data = response2.json()
    assert response_data.get("error") == "Please authenticate.", \
        (f"Expected error message 'Please authenticate.', "
         f"but got {response_data.get('error')}")
