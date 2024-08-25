"""API test Get Contact"""


import pytest
import requests
from tests.api.test_data_api_users import BASE_URL
from test_data.constants import VALID_TOKEN


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


@pytest.fixture
def valid_token():
    """Getting a valid token"""
    valid_token = VALID_TOKEN
    return valid_token


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_get_contact(valid_token, create_contact):
    """Getting contact details"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/contacts/{create_contact}",
                            headers=headers)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    contact_info = response.json()

    assert "_id" in contact_info, \
        "_id missing in response"
    assert "firstName" in contact_info, \
        "_firstName missing in response"
    assert "lastName" in contact_info, \
        "lastName missing in response"
    assert "owner" in contact_info, \
        "owner missing in response"
    assert "__v" in contact_info, \
        "__v missing in response"


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_get_contact_without_auth(valid_token, create_contact):
    """Getting contact details without auth"""
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/contacts/{create_contact}",
                            headers=headers)
    assert response.status_code == 401, (f"Expected status 200, "
                                         f"but got {response.status_code}")


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_get_contact_with_invalid_id(valid_token):
    """Getting contact details with invalid id"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/contacts/123fdg",
                            headers=headers)
    assert response.status_code == 400, (f"Expected status 200, "
                                         f"but got {response.status_code}")
