"""API test Part Update Contact"""


import pytest
import requests
from tests.api.test_data_api_users import BASE_URL
from test_data.constants import VALID_TOKEN



@pytest.fixture
def valid_token():
    """Getting a valid token"""
    valid_token = VALID_TOKEN
    return valid_token


@pytest.fixture
def update_data():
    """Data for updating contacts"""
    return {

    }


def test_update_without_auth(valid_token, update_data):
    """Update contact without auth"""
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 401, (f"Expected status 401, "
                                         f"but got {response.status_code}")


def test_update_first_name(valid_token, update_data):
    """"Update contact first name"""
    update_data["firstName"] = "Alex"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["firstName"] == update_data["firstName"], \
        "First name did not update correctly"


def test_update_last_name(valid_token, update_data):
    """Update contact last name"""
    update_data["lastName"] = "Userovich"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["lastName"] == update_data["lastName"], \
        "Last name did not update correctly"


def test_update_birthdate(valid_token, update_data):
    """Update contact birthdate"""
    update_data["birthdate"] = "1999-12-12"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["birthdate"] == update_data["birthdate"], \
        "Birth Date did not update correctly"


def test_update_email(valid_token, update_data):
    """Update contact email"""
    update_data["email"] = "alex@mail.com"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["email"] == update_data["email"], \
        "Email did not update correctly"


def test_update_phone(valid_token, update_data):
    """Update contact phone"""
    update_data["phone"] = "13535434"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["phone"] == update_data["phone"], \
        "Phone did not update correctly"


def test_update_street1(valid_token, update_data):
    """Update contact street1"""
    update_data["street1"] = "Test Street 1"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["street1"] == update_data["street1"], \
        "Street1 did not update correctly"


def test_update_street2(valid_token, update_data):
    """Update contact street2"""
    update_data["street2"] = "Test Street 2"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["street2"] == update_data["street2"], \
        "Street2 did not update correctly"


def test_update_city(valid_token, update_data):
    """Update contact city"""
    update_data["city"] = "Test City Update"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["city"] == update_data["city"], \
        "City did not update correctly"


def test_update_state(valid_token, update_data):
    """Update contact state"""
    update_data["stateProvince"] = "Test Province Update"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["stateProvince"] == update_data["stateProvince"], \
        "Province did not update correctly"


def test_update_postalcode(valid_token, update_data):
    """Update contact postal code"""
    update_data["postalCode"] = "1354347"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["postalCode"] == update_data["postalCode"], \
        "Postal code did not update correctly"


def test_update_country(valid_token, update_data):
    """Update contact country"""
    update_data["country"] = "1354347"
    headers = {
        "Authorization": f"Bearer {valid_token}",
        "Content-Type": "application/json"
    }
    response = requests.patch(f"{BASE_URL}/contacts/66c50c9a18503e001357c8a4",
                              headers=headers,
                              json=update_data)
    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_json = response.json()
    assert response_json["country"] == update_data["country"], \
        "Country did not update correctly"
