"""PYTEST TEST CASES: CONTACTS"""

import time
import pytest
from pages.contact_list_page import ContactListPage, add_contact_button
from pages.add_contact_page import AddContactPage
import test_data.constants as const
from logger.log_setup import logger


@pytest.mark.priority_high
@pytest.mark.add_contact
def test_create_new_contact(browser_contacts):
    """
    Test the creation of a new contact.
    """
    logger.info("TEST 1: Start execution")
    current_page = ContactListPage(browser_contacts)
    current_page.click_button(add_contact_button)
    current_page = AddContactPage(browser_contacts)
    current_page.complete_add_new_contact(const.FIRST_NAME, const.LAST_NAME,
                                          const.BIRTHDATE, const.EMAIL_ADDRESS,
                                          const.PHONE, const.STREET1,
                                          const.STREET2, const.CITY,
                                          const.STATE_PROVINCE,
                                          const.POSTAL_CODE, const.COUNTRY)
    current_page = ContactListPage(browser_contacts)
    assert current_page.locate_contact_row() is not None
    logger.info("TEST 1: Executed")


@pytest.mark.priority_high
@pytest.mark.add_contact
def test_create_new_contact_without_mandatory_fields(browser_contacts):
    """
    Test the creation of a new contact
    without entering data in mandatory fields.
    """
    logger.info("TEST 2: Start execution")
    current_page = ContactListPage(browser_contacts)
    current_page.click_button(add_contact_button)
    current_page = AddContactPage(browser_contacts)
    current_page.complete_add_new_contact(const.EMPTY_FIELD, const.EMPTY_FIELD,
                                          const.BIRTHDATE, const.EMAIL_ADDRESS,
                                          const.PHONE, const.STREET1,
                                          const.STREET2, const.CITY,
                                          const.STATE_PROVINCE,
                                          const.POSTAL_CODE, const.COUNTRY)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("Contact validation failed: "
                                  "firstName: Path `firstName` is required., "
                                  "lastName: Path `lastName` is required.")
    time.sleep(5)
    logger.info("TEST 2: Executed")


@pytest.mark.priority_medium
@pytest.mark.add_contact
def test_create_new_contact_with_invalid_characters(browser_contacts):
    """
    Test the creation of a new contact
    with entering invalid type of characters
    to fields that do not accepts such characters
    """
    logger.info("TEST 3: Start execution")
    current_page = ContactListPage(browser_contacts)
    current_page.click_button(add_contact_button)
    current_page = AddContactPage(browser_contacts)
    (current_page.
     complete_add_new_contact(const.FIRST_NAME, const.LAST_NAME,
                              const.INVALID_CHARACTERS_BIRTHDATE,
                              const.INVALID_CHARACTERS_EMAIL_ADDRESS,
                              const.INVALID_CHARACTERS_PHONE,
                              const.STREET1, const.STREET2, const.CITY,
                              const.STATE_PROVINCE,
                              const.INVALID_CHARACTERS_POSTAL_CODE,
                              const.COUNTRY))
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("Contact validation failed: "
                                  "birthdate: Birthdate is invalid, "
                                  "email: Email is invalid, "
                                  "phone: Phone number is invalid, "
                                  "postalCode: Postal code is invalid")
    time.sleep(5)
    logger.info("TEST 3: Executed")


@pytest.mark.priority_medium
@pytest.mark.add_contact
def test_create_new_contact_max_amount_of_characters_exceeded(
        browser_contacts):
    """
    Test the creation of a new contact
    with exceeding the maximum amount of charcters
    in the text fields
    """
    logger.info("TEST 4: Start execution")
    current_page = ContactListPage(browser_contacts)
    current_page.click_button(add_contact_button)
    current_page = AddContactPage(browser_contacts)
    (current_page.
     complete_add_new_contact(const.LONG_FIRST_NAME, const.LONG_LAST_NAME,
                              const.BIRTHDATE, const.EMAIL_ADDRESS,
                              const.LONG_PHONE,
                              const.LONG_STREET1, const.LONG_STREET2,
                              const.LONG_CITY, const.LONG_STATE_PROVINCE,
                              const.LONG_POSTAL_CODE, const.LONG_COUNTRY))
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert (validation_message ==
            ("Contact validation failed: "
             "firstName: Path `firstName` (`Abcdefghijklmnopqrstu`) "
             "is longer than the maximum allowed length (20)., "
             "lastName: Path `lastName` (`Abcdefghijklmnopqrstu`) "
             "is longer than the maximum allowed length (20)., "
             "phone: Path `phone` (`1234567890123456`) "
             "is longer than the maximum allowed length (15)., "
             "street1: Path `street1` "
             "(`AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno`) "
             "is longer than the maximum allowed length (40)., "
             "street2: Path `street2` "
             "(`AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno`) "
             "is longer than the maximum allowed length (40)., "
             "city: Path `city` "
             "(`AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno`) "
             "is longer than the maximum allowed length (40)., "
             "stateProvince: Path `stateProvince` (`Abcdefghijklmnopqrstu`) "
             "is longer than the maximum allowed length (20)., "
             "postalCode: Path `postalCode` (`12345678901`) "
             "is longer than the maximum allowed length (10)., "
             "country: Path `country` "
             "(`AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno`) "
             "is longer than the maximum allowed length (40)."))
    time.sleep(5)
    logger.info("TEST 4: Executed")
