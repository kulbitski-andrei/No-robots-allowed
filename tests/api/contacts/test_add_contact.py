"""API test Add Contact"""

import requests
import pytest
from tests.api.contacts.test_data_api_contacts import BASE_URL


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_create_contact_success(valid_token, contact_data):
    """Successful creation of a contact."""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f"{BASE_URL}/contacts",
                             headers=headers, json=contact_data)

    assert response.status_code == 201, \
        f"Expected 201, but got {response.status_code}"


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_create_contact_missing_required_fields(valid_token):
    """Creating a contact with missing required fields."""
    incomplete_contact_data = {
        "lastName": "Doe"
    }

    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f"{BASE_URL}/contacts",
                             headers=headers, json=incomplete_contact_data)

    assert response.status_code == 400, (f"Expected 400, "
                                         f"but got {response.status_code}")


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_create_contact_invalid_email(valid_token, contact_data):
    """Creating a contact with invalid email."""
    contact_data["email"] = "failed_emai@sss"

    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f"{BASE_URL}/contacts",
                             headers=headers, json=contact_data)

    assert response.status_code == 400, (f"Expected 400,"
                                         f" but got {response.status_code}")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_create_contact_unauthorized():
    """Creating a contact without authorization."""
    contact_data = {
        "firstName": "John",
        "lastName": "Doe"
    }

    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(f"{BASE_URL}/contacts",
                             headers=headers, json=contact_data)

    assert response.status_code == 401, (f"Expected 401,"
                                         f" but got {response.status_code}")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_create_contact_invalid_phone(valid_token, contact_data):
    """Creating a contact with invalid phone number."""
    contact_data["phone"] = "1354315343543"

    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f"{BASE_URL}/contacts",
                             headers=headers, json=contact_data)

    assert response.status_code == 400, (f"Expected 400,"
                                         f" but got {response.status_code}")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_create_contact_invalid_birthdate(valid_token, contact_data):
    """Creating a contact with invalid date of birth."""
    contact_data["birthdate"] = "12/12/1999"

    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f"{BASE_URL}/contacts",
                             headers=headers, json=contact_data)

    assert response.status_code == 400, (f"Expected 400,"
                                         f" but got {response.status_code}")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_create_contact_invalid_postalcode(valid_token, contact_data):
    """Creating a contact with invalid postal code."""
    contact_data["postalCode"] = "1351564599"

    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(f"{BASE_URL}/contacts",
                             headers=headers, json=contact_data)

    assert response.status_code == 400, (f"Expected 400, "
                                         f"but got {response.status_code}")
