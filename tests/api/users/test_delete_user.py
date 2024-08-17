import pytest
import requests
from tests.api.test_data_api_users import BASE_URL, HEADERS, UserData


@pytest.fixture
def auth_token_and_user_data():
    """Fixture to register a user and obtain an auth token."""
    user_data = UserData.generate_user_data()  # Получение данных пользователя из UserData

    # Регистрация нового пользователя
    response = requests.post(f"{BASE_URL}/users", json=user_data, headers=HEADERS)
    assert response.status_code == 201, f"Expected status 201, but got {response.status_code}"

    # Логин с зарегистрированным пользователем
    login_data = {
        "email": user_data["email"],
        "password": user_data["password"]
    }
    login_response = requests.post(f"{BASE_URL}/users/login", json=login_data, headers=HEADERS)
    assert login_response.status_code == 200, f"Expected status 200, but got {login_response.status_code}"

    response_data = login_response.json()
    return {
        "token": response_data["token"],
        "user_data": user_data
    }


def test_delete_user(auth_token_and_user_data):
    """Positive test: Successfully delete a user."""
    token = auth_token_and_user_data["token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = requests.delete(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 200, f"Expected status 200, but got {response.status_code}"
    assert response.text == "", "Expected empty response body for successful delete"


def test_delete_user_invalid_token():
    """Negative test: Attempt to delete a user with an invalid token."""
    invalid_token = "invalid_token"
    headers = {
        "Authorization": f"Bearer {invalid_token}"
    }

    response = requests.delete(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 401, f"Expected status 401, but got {response.status_code}"
    response_data = response.json()
    assert response_data.get("error") == "Please authenticate.", f"Expected error message 'Please authenticate.', but got {response_data.get('error')}"


def test_delete_user_twice(auth_token_and_user_data):
    """Negative test: Attempt to delete a user twice."""
    token = auth_token_and_user_data["token"]
    headers = {
        "Authorization": f"Bearer {token}"
    }

    # Первый запрос на удаление
    response1 = requests.delete(f"{BASE_URL}/users/me", headers=headers)
    assert response1.status_code == 200, f"Expected status 200, but got {response1.status_code}"
    assert response1.text == "", "Expected empty response body for successful delete"

    # Попытка удалить снова
    response2 = requests.delete(f"{BASE_URL}/users/me", headers=headers)
    assert response2.status_code == 401, f"Expected status 401, but got {response2.status_code}"
    response_data = response2.json()
    assert response_data.get("error") == "Please authenticate.", f"Expected error message 'Please authenticate.', but got {response_data.get('error')}"


def test_delete_user_non_existent(auth_token_and_user_data):
    """Negative test: Attempt to delete a non-existent user."""
    # Эмуляция недействительного токена для удаления
    invalid_token = "invalid_token"
    headers = {
        "Authorization": f"Bearer {invalid_token}"
    }

    response = requests.delete(f"{BASE_URL}/users/me", headers=headers)

    assert response.status_code == 401, f"Expected status 401, but got {response.status_code}"
    assert response.text == '{"error":"Please authenticate."}', "Expected error message for unauthorized access"
