"""API test Get Contact"""

import pytest
import requests
from tests.api.contacts.test_data_api_contacts import BASE_URL


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_get_list_contacts(valid_token):
    """Getting a list of contacts"""
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/contacts",
                            headers=headers)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_get_list_contacts_without_auth(valid_token):
    """Getting a list of contacts without auth"""
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/contacts",
                            headers=headers)
    assert response.status_code == 401, (f"Expected status 200, "
                                         f"but got {response.status_code}")
