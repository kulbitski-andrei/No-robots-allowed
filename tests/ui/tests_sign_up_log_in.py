"""PYTEST TEST CASES: SIGN UP, LOG IN"""

import time
import pytest
from pages.login_page import LoginPage
from pages.signup_page import SignupPage
# from conftest import browser_sign_up_log_in
import test_data.constants as const
from logger.log_setup import logger


@pytest.mark.log_in_invalid_password
def test_log_in_invalid_password(browser_sign_up_log_in):
    """
    Test the attempt to log in with valid email and invalid password.
    """
    logger.info("TEST 1: Start execution")
    page_object = LoginPage(browser_sign_up_log_in)
    time.sleep(1)
    page_object.complete_login(const.EMAIL, const.WRONG_PASSWORD)
    time.sleep(1)
    validation_message = page_object.locate_validation_message()
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
    page_object = LoginPage(browser_sign_up_log_in)
    time.sleep(2)
    page_object.click_submit()
    time.sleep(1)
    validation_message = page_object.locate_validation_message()
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
    page_object = LoginPage(browser_sign_up_log_in)
    page_object.click_sign_up()
    time.sleep(1)
    page_object = SignupPage(browser_sign_up_log_in)
    page_object.complete_signup(const.USER_FIRST_NAME,
                                const.USER_LAST_NAME,
                                const.EMAIL,
                                const.WRONG_PASSWORD)
    time.sleep(1)
    validation_message = page_object.locate_validation_message()
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
    page_object = LoginPage(browser_sign_up_log_in)
    page_object.click_sign_up()
    time.sleep(1)
    page_object = SignupPage(browser_sign_up_log_in)
    page_object.complete_signup(const.USER_FIRST_NAME,
                                const.USER_LAST_NAME,
                                const.INVALID_EMAIL,
                                const.WRONG_PASSWORD)
    time.sleep(1)
    validation_message = page_object.locate_validation_message()
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
    page_object = LoginPage(browser_sign_up_log_in)
    page_object.click_sign_up()
    time.sleep(1)
    page_object = SignupPage(browser_sign_up_log_in)
    time.sleep(1)
    page_object.click_submit()
    time.sleep(1)  # This one is really needed!
    validation_message = page_object.locate_validation_message()
    time.sleep(1)
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("User validation failed: "
                                  "firstName: Path `firstName` is required., "
                                  "lastName: Path `lastName` is required., "
                                  "email: Email is invalid, "
                                  "password: Path `password` is required.")
    logger.info("TEST 5: Executed")
