"""API tests Delete Contact"""

import pytest
import requests
from tests.api.contacts.test_data_api_contacts import BASE_URL


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_delete_contact_twice(valid_token):
    """Deleting a contact twice"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.delete(f"{BASE_URL}/contacts/66c5359f18503e001357c8d1",
                               headers=headers)
    assert response.status_code == 404, (f"Expected status 404, "
                                         f"but got {response.status_code}")


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
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


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
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


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_delete_contact_without_auth(valid_token):
    """Deleting a contact without auth"""
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.delete(f"{BASE_URL}/contacts/dasfadga",
                               headers=headers)
    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")
