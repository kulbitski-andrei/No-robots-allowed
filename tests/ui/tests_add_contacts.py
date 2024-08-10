"""PYTEST TEST CASES: CONTACTS"""

import time
import pytest
from pages.contact_list_page import ContactListPage
from pages.add_contact_page import AddContactPage
import test_data.constants as const
from logger.log_setup import logger


@pytest.mark.create_new_contact
def test_create_new_contact(browser_contacts):
    """
    Test the creation of a new contact.
    """
    logger.info("TEST 1: Start execution")
    page_object = ContactListPage(browser_contacts)
    page_object.click_add_contact()
    page_object = AddContactPage(browser_contacts)
    page_object.complete_add_new_contact(const.FIRST_NAME, const.LAST_NAME,
                                         const.BIRTHDATE, const.EMAIL_ADDRESS,
                                         const.PHONE, const.STREET1,
                                         const.STREET2, const.CITY,
                                         const.STATE_PROVINCE,
                                         const.POSTAL_CODE, const.COUNTRY)
    page_object = ContactListPage(browser_contacts)
    assert page_object.locate_contact_row() is not None
    logger.info("TEST 1: Executed")


@pytest.mark.create_new_contact_without_mandatory_fields
def test_create_new_contact_without_mandatory_fields(browser_contacts):
    logger.info("TEST 2: Start execution")
    page_object = ContactListPage(browser_contacts)
    page_object.click_add_contact()
    page_object = AddContactPage(browser_contacts)
    page_object.complete_add_new_contact(const.EMPTY_FIELD, const.EMPTY_FIELD,
                                         const.BIRTHDATE, const.EMAIL_ADDRESS,
                                         const.PHONE, const.STREET1,
                                         const.STREET2, const.CITY,
                                         const.STATE_PROVINCE,
                                         const.POSTAL_CODE, const.COUNTRY)
    validation_message = page_object.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("Contact validation failed: "
                                  "firstName: Path `firstName` is required., "
                                  "lastName: Path `lastName` is required.")
    time.sleep(5)
    logger.info("TEST 2: Executed")


@pytest.mark.create_new_contact_with_invalid_characters
def test_create_new_contact_with_invalid_characters(browser_contacts):
    logger.info("TEST 3: Start execution")
    page_object = ContactListPage(browser_contacts)
    page_object.click_add_contact()
    page_object = AddContactPage(browser_contacts)
    page_object.complete_add_new_contact(const.FIRST_NAME, const.LAST_NAME,
                                         const.INVALID_CHARACTERS_BIRTHDATE,
                                         const.INVALID_CHARACTERS_EMAIL_ADDRESS,
                                         const. INVALID_CHARACTERS_PHONE,
                                         const.STREET1, const.STREET2, const.CITY,
                                         const.STATE_PROVINCE,
                                         const.INVALID_CHARACTERS_POSTAL_CODE,
                                         const.COUNTRY)
    time.sleep(1)
    validation_message = page_object.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("Contact validation failed: "
                                  "birthdate: Birthdate is invalid, "
                                  "email: Email is invalid, "
                                  "phone: Phone number is invalid, "
                                  "postalCode: Postal code is invalid")
    time.sleep(10)
    logger.info("TEST 3: Executed")


@pytest.mark.create_new_contact_max_amount_of_characters_exceeded
def test_create_new_contact_max_amount_of_characters_exceeded(browser_contacts):
    logger.info("TEST 4: Start execution")
    page_object = ContactListPage(browser_contacts)
    page_object.click_add_contact()
    page_object = AddContactPage(browser_contacts)
    page_object.complete_add_new_contact(const.FIRST_NAME, const.LAST_NAME,
                                         const.INVALID_CHARACTERS_BIRTHDATE,
                                         const.INVALID_CHARACTERS_EMAIL_ADDRESS,
                                         const. INVALID_CHARACTERS_PHONE,
                                         const.STREET1, const.STREET2, const.CITY,
                                         const.STATE_PROVINCE,
                                         const.INVALID_CHARACTERS_POSTAL_CODE,
                                         const.COUNTRY)
    time.sleep(1)
    validation_message = page_object.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("Contact validation failed: "
                                  "birthdate: Birthdate is invalid, "
                                  "email: Email is invalid, "
                                  "phone: Phone number is invalid, "
                                  "postalCode: Postal code is invalid")
    time.sleep(10)
    logger.info("TEST 4: Executed")