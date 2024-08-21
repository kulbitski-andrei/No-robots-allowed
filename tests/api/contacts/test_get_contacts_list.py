import pytest

from tests.api.test_data_api_users import BASE_URL
from test_data.constants import VALID_TOKEN
import requests


@pytest.fixture
def valid_token():
    """Getting a valid token"""
    valid_token = VALID_TOKEN
    return valid_token


def test_get_list_contacts(valid_token):
    """Getting a list of contacts"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/contacts", headers=headers)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")


def test_get_list_contacts_without_auth(valid_token):
    """Getting a list of contacts without auth"""
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/contacts", headers=headers)
    assert response.status_code == 401, (f"Expected status 200, "
                                         f"but got {response.status_code}")
