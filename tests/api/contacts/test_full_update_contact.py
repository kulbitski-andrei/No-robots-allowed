"""API test Full Update Contact"""

import pytest
from tests.api.test_data_api_users import BASE_URL
from test_data.constants import VALID_TOKEN
import requests


@pytest.fixture
def valid_token():
    """API test Add user"""
    valid_token = VALID_TOKEN
    return valid_token


@pytest.fixture
def update_data():
    """Update data"""
    return {
        "firstName": "Tester",
        "lastName": "Test",
        "birthdate": "1992-02-02",
        "email": "tester@fake.com",
        "phone": "8005554242",
        "street1": "13 School St.",
        "street2": "Apt. 5",
        "city": "Washington",
        "stateProvince": "QC",
        "postalCode": "A1A1A1",
        "country": "Canada"
    }


def test_full_update_contact(valid_token, update_data):
    """Successfull update Contact"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.put(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4", headers=headers,
                            json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()

    assert response_json["firstName"] == update_data["firstName"], \
        "First name did not update correctly"
    assert response_json["lastName"] == update_data["lastName"], \
        "Last Name did not update correctly"
    assert response_json["birthdate"] == update_data["birthdate"], \
        "Birth Date did not update correctly"
    assert response_json["email"] == update_data["email"], \
        "Email did not update correctly"
    assert response_json["phone"] == update_data["phone"], \
        "Phone did not update correctly"
    assert response_json["street1"] == update_data["street1"], \
        "Street1 did not update correctly"
    assert response_json["street2"] == update_data["street2"], \
        "Street2 did not update correctly"
    assert response_json["city"] == update_data["city"], \
        "City did not update correctly"
    assert response_json["stateProvince"] == update_data["stateProvince"], \
        "State Province did not update correctly"
    assert response_json["postalCode"] == update_data["postalCode"], \
        "Postal Code did not update correctly"
    assert response_json["country"] == update_data["country"], \
        "Country did not update correctly"


def test_full_update_contact_without_auth(valid_token, update_data):
    """Update contact without auth"""
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4", headers=headers,
                            json=update_data)
    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")


def test_full_update_contact_with_invalid_field(valid_token, update_data):
    """Update contact without invalid field"""
    update_data["email"] = "failed_emai@sss"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.put(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4", headers=headers,
                            json=update_data)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")


def test_full_update_contact_with_empty_field(valid_token, update_data):
    """Update contact with empty field"""
    update_data["phone"] = ""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.put(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4", headers=headers,
                            json=update_data)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")