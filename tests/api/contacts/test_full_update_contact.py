"""API test Full Update Contact"""

import pytest
import requests
from tests.api.contacts.test_data_api_contacts import BASE_URL


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_full_update_contact(valid_token, update_data, create_contact):
    """Successful update Contact"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.put(f"{BASE_URL}/contacts/{create_contact}",
                            headers=headers,
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


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_full_update_contact_without_auth(valid_token,
                                          update_data, create_contact):
    """Update contact without auth"""
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.put(f"{BASE_URL}/contacts/{create_contact}",
                            headers=headers,
                            json=update_data)
    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_full_update_contact_with_invalid_field(valid_token,
                                                update_data, create_contact):
    """Update contact without invalid field"""
    update_data["email"] = "failed_emai@sss"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.put(f"{BASE_URL}/contacts/{create_contact}",
                            headers=headers,
                            json=update_data)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_full_update_contact_with_empty_field(valid_token,
                                              update_data, create_contact):
    """Update contact with empty field"""
    update_data["phone"] = ""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.put(f"{BASE_URL}/contacts/{create_contact}",
                            headers=headers,
                            json=update_data)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")
