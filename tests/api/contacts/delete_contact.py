"""API test Delete Contact"""

import pytest
import requests
from tests.api.test_data_api_users import BASE_URL
from test_data.constants import VALID_TOKEN


@pytest.fixture
def valid_token():
    """API test Add user"""
    valid_token = VALID_TOKEN
    return valid_token


@pytest.fixture
def create_contact(valid_token):
    """Create contact"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f"{BASE_URL}/contacts",
                             headers=headers, json={"firstName": "John",
                                                    "lastName": "Doe"})
    response = response.json()
    contact_id = response["_id"]
    return contact_id


def test_delete_contact_twice(valid_token):
    """Deleting a unexisting contact should fail"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.delete(f"{BASE_URL}/contacts/66c5359f18503e001357c8d1",
                               headers=headers)
    assert response.status_code == 404, (f"Expected status 404, "
                                         f"but got {response.status_code}")


def test_delete_contact(valid_token, create_contact):
    """Deleting a contact should succeed"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.delete(f"{BASE_URL}/contacts/{create_contact}",
                               headers=headers)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")


def test_delete_contact_with_invalid_id(valid_token):
    """Deleting a contact with invalid id"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.delete(f"{BASE_URL}/contacts/dasfadga",
                               headers=headers)
    assert response.status_code == 400, (f"Expected status 400,"
                                         f" "
                                         f"but got {response.status_code}")


def test_delete_contact_without_auth(valid_token):
    """Deleting a contact without auth"""
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(f"{BASE_URL}/contacts/dasfadga",
                               headers=headers)
    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
