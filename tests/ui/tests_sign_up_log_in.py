"""PYTEST TEST CASES: SIGN UP, LOG IN, LOG OUT"""

import time
import pytest
from pages.base_page import logout_button
from pages.login_page import LoginPage, submit_button, signup_button
from pages.contact_list_page import ContactListPage
from pages.signup_page import SignupPage
import test_data.constants as const
from test_data.service_methods import generate_random_email
from logger.log_setup import logger


@pytest.mark.priority_high
@pytest.mark.ui_log_in
def test_log_in_valid_credentials(browser_sign_up_log_in):
    """
    Test if user is able to login with correct login and password.
    """
    logger.info("TEST 1: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.complete_login(const.EMAIL, const.PASSWORD)
    current_page = ContactListPage(browser_sign_up_log_in)
    time.sleep(1)  # This one is really needed!
    uniform_resource_locator = browser_sign_up_log_in.current_url
    page_title = browser_sign_up_log_in.title
    page_header = current_page.locate_page_header_title().text
    logger.info(f"URL: {uniform_resource_locator}")
    logger.info(f"PAGE TITLE: {page_title}")
    logger.info(f"PAGE HEADER: {page_header}")
    assert (uniform_resource_locator ==
            "https://thinking-tester-contact-list.herokuapp.com/contactList")
    assert page_title == "My Contacts"
    assert page_header == "Contact List"
    logger.info("TEST 1: Executed")


@pytest.mark.priority_high
@pytest.mark.ui_log_in
def test_log_in_icorrect_password(browser_sign_up_log_in):
    """
    Test the attempt to log in with valid email and invalid password.
    """
    logger.info("TEST 2: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.complete_login(const.EMAIL, const.WRONG_PASSWORD)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == "Incorrect username or password"
    logger.info("TEST 2: Executed")


@pytest.mark.priority_medium
@pytest.mark.ui_log_in
def test_log_in_empty_fields(browser_sign_up_log_in):
    """
    Test the attempt to log in with empty email and password fields.
    """
    logger.info("TEST 3: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.click_button(submit_button)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == "Incorrect username or password"
    logger.info("TEST 3: Executed")


@pytest.mark.priority_high
@pytest.mark.ui_sign_up
def test_sign_up_with_valid_credentials(browser_sign_up_log_in):
    """
    Test if it's able to create a new user login and password.
    """
    logger.info("TEST 4: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.click_button(signup_button)
    current_page = SignupPage(browser_sign_up_log_in)
    current_page.complete_signup(const.USER_FIRST_NAME,
                                 const.USER_LAST_NAME,
                                 generate_random_email(),
                                 const.PASSWORD)
    current_page = ContactListPage(browser_sign_up_log_in)
    time.sleep(1)  # This one is really needed!
    uniform_resource_locator = browser_sign_up_log_in.current_url
    page_title = browser_sign_up_log_in.title
    page_header = current_page.locate_page_header_title().text
    logger.info(f"URL: {uniform_resource_locator}")
    logger.info(f"PAGE TITLE: {page_title}")
    logger.info(f"PAGE HEADER: {page_header}")
    assert (uniform_resource_locator ==
            "https://thinking-tester-contact-list.herokuapp.com/contactList")
    assert page_title == "My Contacts"
    assert page_header == "Contact List"
    logger.info("TEST 4: Executed")


@pytest.mark.priority_high
@pytest.mark.ui_sign_up
def test_sign_up_with_existing_email(browser_sign_up_log_in):
    """
    Test the attempt to log in with existing email.
    """
    logger.info("TEST 5: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.click_button(signup_button)
    current_page = SignupPage(browser_sign_up_log_in)
    current_page.complete_signup(const.USER_FIRST_NAME,
                                 const.USER_LAST_NAME,
                                 const.EMAIL,
                                 const.PASSWORD)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == "Email address is already in use"
    logger.info("TEST 5: Executed")


@pytest.mark.priority_high
@pytest.mark.ui_sign_up
def test_sign_up_with_invalid_email(browser_sign_up_log_in):
    """
    Test the attempt to log in with invalid email.
    """
    logger.info("TEST 6: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.click_button(signup_button)
    current_page = SignupPage(browser_sign_up_log_in)
    current_page.complete_signup(const.USER_FIRST_NAME,
                                 const.USER_LAST_NAME,
                                 const.INVALID_EMAIL,
                                 const.WRONG_PASSWORD)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("User validation failed: email: "
                                  "Email is invalid")
    logger.info("TEST 6: Executed")


@pytest.mark.priority_medium
@pytest.mark.ui_sign_up
def test_sign_up_empty_fields(browser_sign_up_log_in):
    """
    Test the attempt to sign up with empty form.
    """
    logger.info("TEST 7: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.click_button(signup_button)
    current_page = SignupPage(browser_sign_up_log_in)
    current_page.click_button(submit_button)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("User validation failed: "
                                  "firstName: Path `firstName` is required., "
                                  "lastName: Path `lastName` is required., "
                                  "email: Email is invalid, "
                                  "password: Path `password` is required.")
    logger.info("TEST 7: Executed")


@pytest.mark.priority_medium
@pytest.mark.ui_log_out
def test_log_out(browser_sign_up_log_in):
    """
    Test of logging out from the system.
    """
    logger.info("TEST 8: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.complete_login(const.EMAIL, const.PASSWORD)
    current_page = ContactListPage(browser_sign_up_log_in)
    time.sleep(1)  # This one is really needed!
    uniform_resource_locator = browser_sign_up_log_in.current_url
    assert (uniform_resource_locator ==
            "https://thinking-tester-contact-list.herokuapp.com/contactList")
    current_page.click_button(logout_button)
    time.sleep(1)  # This one is really needed!
    uniform_resource_locator = browser_sign_up_log_in.current_url
    page_title = browser_sign_up_log_in.title
    page_header = current_page.locate_page_header_title().text
    logger.info(f"URL: {uniform_resource_locator}")
    logger.info(f"PAGE TITLE: {page_title}")
    logger.info(f"PAGE HEADER: {page_header}")
    assert (uniform_resource_locator ==
            "https://thinking-tester-contact-list.herokuapp.com/")
    assert page_title == "Contact List App"
    assert page_header == "Contact List App"
    logger.info("TEST 8: Executed")
