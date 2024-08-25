"""API tests Update user"""


import requests
import pytest
from tests.api.users.data_api_users import BASE_URL, HEADERS, UserData


@pytest.mark.high
@pytest.mark.smoke
@pytest.mark.API
def test_update_user_profile_success(auth_token_and_user_data):
    """Positive tests: Successfully update user profile information."""
    auth_token, _ = auth_token_and_user_data
    update_data = UserData.generate_user_data()

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.patch(f"{BASE_URL}/users/me",
                              json=update_data, headers=headers)

    assert response.status_code == 200, (f"Expected status 200, "
                                         f"but got {response.status_code}")
    response_data = response.json()

    assert response_data["firstName"] == update_data["firstName"], \
        "First name did not update correctly"
    assert response_data["lastName"] == update_data["lastName"], \
        "Last name did not update correctly"
    assert response_data["email"] == update_data["email"], \
        "Email did not update correctly"


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_update_user_profile_existing_email(auth_token_and_user_data):
    """Negative tests: Attempt to update user profile with an existing email."""
    auth_token, user_data = auth_token_and_user_data

    existing_user_data = UserData.generate_user_data()
    response = requests.post(f"{BASE_URL}/users",
                             json=existing_user_data, headers=HEADERS)
    assert response.status_code == 201, (f"Expected status 201, "
                                         f"but got {response.status_code}")

    response_data = response.json()
    print("Response Data from User Creation:", response_data)  # For debugging

    existing_email = response_data.get("user", {}).get("email")
    assert existing_email is not None, "Expected 'email' in the response data"

    update_data = UserData.generate_user_data()
    update_data["email"] = existing_email

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.patch(f"{BASE_URL}/users/me",
                              json=update_data, headers=headers)
    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")
    response_data = response.json()
    print("Response Data from Update Attempt:", response_data)  # For debugging

    assert "name" in response_data and response_data["name"] == "MongoError", \
        "Expected MongoError in the response data"
    assert "code" in response_data and response_data["code"] == 11000, \
        "Expected error code 11000 for unique index violation"
    assert ("keyValue" in response_data and
            response_data["keyValue"].get("email") ==
            existing_email), "Expected existing email in the error details"


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_update_user_profile_malformed_email(auth_token_and_user_data):
    """Negative tests: Attempt to update user profile with a malformed email."""
    auth_token, _ = auth_token_and_user_data

    update_data = UserData.generate_user_data()
    update_data["email"] = "invalid-email-format"

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.patch(f"{BASE_URL}/users/me",
                              json=update_data, headers=headers)

    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")
    response_data = response.json()
    print("Response Data from Update Attempt:", response_data)

    assert "_message" in response_data, \
        "Expected '_message' in the response data"
    assert response_data["_message"] == "User validation failed", \
        "Unexpected '_message' value"

    assert "errors" in response_data, "Expected 'errors' in the response data"
    assert "email" in response_data["errors"], \
        "Expected 'email' key in 'errors'"
    assert response_data["errors"]["email"]["message"] == "Email is invalid", \
        "Unexpected error message for 'email'"
    assert (response_data["errors"]["email"]["value"] ==
            "invalid-email-format"), \
        "Unexpected value for 'email' error"


@pytest.mark.medium
@pytest.mark.regress
@pytest.mark.API
def test_update_user_profile_weak_password(auth_token_and_user_data):
    """Negative tests: Attempt to update user profile with a weak password."""
    auth_token, _ = auth_token_and_user_data

    update_data = UserData.generate_user_data()
    update_data["password"] = "short"

    headers = {
        "Authorization": f"Bearer {auth_token}"
    }

    response = requests.patch(f"{BASE_URL}/users/me",
                              json=update_data, headers=headers)

    assert response.status_code == 400, (f"Expected status 400, "
                                         f"but got {response.status_code}")
    response_data = response.json()
    print("Response Data from Update Attempt:", response_data)

    assert "_message" in response_data, ("Expected '_message' "
                                         "in the response data")
    assert response_data["_message"] == ("User validation "
                                         "failed"), ("Unexpected "
                                                     "'_message' value")

    assert "errors" in response_data, ("Expected 'errors' "
                                       "in the response data")
    assert "password" in response_data["errors"], \
        "Expected 'password' key in 'errors'"
    assert (response_data["errors"]["password"]["message"] ==
            ("Path `password` (`short`) is shorter than the minimum "
             "allowed length (7).")), "Unexpected error message for 'password'"
    assert response_data["errors"]["password"]["value"] == "short", \
        "Unexpected value for 'password' error"
