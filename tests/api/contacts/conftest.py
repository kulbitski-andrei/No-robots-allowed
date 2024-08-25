"""Fixtures API"""


import uuid
import pytest
import requests
from tests.api.contacts.test_data_api_contacts import BASE_URL


@pytest.fixture
def valid_token():
    """Get a valid token."""
    headers = {
        "Content-Type": "application/json"
    }
    unique_email = f"test_user_{uuid.uuid4()}@fake.com"
    response = requests.post(f"{BASE_URL}/users", headers=headers, json={
        "firstName": "Test",
        "lastName": "User",
        "email": unique_email,
        "password": "myPassword"
        })
    data = response.json()
    valid_token = data["token"]
    return valid_token


@pytest.fixture
def contact_data():
    """Contact data fixture"""
    return {
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }


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
