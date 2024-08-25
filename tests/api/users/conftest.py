"""Fixtures API"""


import pytest
import requests
from test_data.test_data_api_users import BASE_URL, HEADERS, UserData


@pytest.fixture
def auth_token_and_user_data():
    """Fixture to register a user and obtain an auth token."""
    user_data = UserData.generate_user_data()

    response = requests.post(f"{BASE_URL}/users",
                             json=user_data, headers=HEADERS)
    assert response.status_code == 201, (f"Expected status 201, "
                                         f"but got {response.status_code}")

    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_response = requests.post(f"{BASE_URL}/users/login",
                                   json=login_data, headers=HEADERS)
    assert login_response.status_code == 200, \
        f"Expected status 200, but got {login_response.status_code}"

    response_data = login_response.json()
    # return {
    #     "token": response_data["token"],
    #     "user_data": user_data
    # }
    return response_data["token"], user_data
