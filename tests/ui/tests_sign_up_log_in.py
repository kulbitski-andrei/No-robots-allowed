"""PYTEST TEST CASES: SIGN UP, LOG IN"""

import time
import pytest
from pages.login_page import LoginPage, submit_button, signup_button
from pages.signup_page import SignupPage
import test_data.constants as const
from logger.log_setup import logger


@pytest.mark.log_in_invalid_password
def test_log_in_invalid_password(browser_sign_up_log_in):
    """
    Test the attempt to log in with valid email and invalid password.
    """
    logger.info("TEST 1: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    time.sleep(1)
    current_page.complete_login(const.EMAIL, const.WRONG_PASSWORD)
    time.sleep(1)
    validation_message = current_page.locate_validation_message()
    time.sleep(1)
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == "Incorrect username or password"
    time.sleep(1)
    logger.info("TEST 1: Executed")


@pytest.mark.log_in_empty_fields
def test_log_in_empty_fields(browser_sign_up_log_in):
    """
    Test the attempt to log in with empty email and password fields.
    """
    logger.info("TEST 2: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    time.sleep(2)
    current_page.click_button(submit_button)
    time.sleep(1)
    validation_message = current_page.locate_validation_message()
    time.sleep(1)
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == "Incorrect username or password"
    logger.info("TEST 2: Executed")


@pytest.mark.test_sign_up_with_existing_email
def test_sign_up_with_existing_email(browser_sign_up_log_in):
    """
    Test the attempt to log in with existing email.
    """
    logger.info("TEST 3: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.click_button(signup_button)
    time.sleep(1)
    current_page = SignupPage(browser_sign_up_log_in)
    current_page.complete_signup(const.USER_FIRST_NAME,
                                 const.USER_LAST_NAME,
                                 const.EMAIL,
                                 const.WRONG_PASSWORD)
    time.sleep(1)
    validation_message = current_page.locate_validation_message()
    time.sleep(1)
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    time.sleep(1)
    assert validation_message == "Email address is already in use"
    logger.info("TEST 3: Executed")


@pytest.mark.test_sign_up_with_invalid_email
def test_sign_up_with_invalid_email(browser_sign_up_log_in):
    """
    Test the attempt to log in with invalid email.
    """
    logger.info("TEST 4: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.click_button(signup_button)
    time.sleep(1)
    current_page = SignupPage(browser_sign_up_log_in)
    current_page.complete_signup(const.USER_FIRST_NAME,
                                 const.USER_LAST_NAME,
                                 const.INVALID_EMAIL,
                                 const.WRONG_PASSWORD)
    time.sleep(1)
    validation_message = current_page.locate_validation_message()
    time.sleep(1)
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    time.sleep(1)
    assert validation_message == ("User validation failed: email: "
                                  "Email is invalid")
    logger.info("TEST 4: Executed")


@pytest.mark.sign_up_empty_fields
def test_sign_up_empty_fields(browser_sign_up_log_in):
    """
    Test the attempt to sign up with empty form.
    """
    logger.info("TEST 5: Start execution")
    current_page = LoginPage(browser_sign_up_log_in)
    current_page.click_button(signup_button)
    time.sleep(1)
    current_page = SignupPage(browser_sign_up_log_in)
    time.sleep(1)
    current_page.click_button(submit_button)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    time.sleep(1)
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("User validation failed: "
                                  "firstName: Path `firstName` is required., "
                                  "lastName: Path `lastName` is required., "
                                  "email: Email is invalid, "
                                  "password: Path `password` is required.")
    logger.info("TEST 5: Executed")
