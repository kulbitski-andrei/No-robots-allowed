"""PYTEST TEST CASES: CONTACTS"""

import time
import pytest
from pages.contact_list_page import ContactListPage
from pages.contact_details_page import ContactDetailsPage, edit_button
from pages.edit_contact_page import (EditContactPage, first_name_field,
                                     last_name_field, birthdate_field,
                                     email_address_field, phone_field,
                                     street1_field, street2_field,
                                     city_field, state_province_field,
                                     postal_code_field, country_field)
import test_data.constants as const
from logger.log_setup import logger


@pytest.mark.edit_contact
def test_edit_contact(browser_contacts):
    """
    Test the editing of an existing contact.
    """
    logger.info("TEST 1: Start execution")
    current_page = ContactListPage(browser_contacts)
    current_page.open_contact()
    current_page = ContactDetailsPage(browser_contacts)
    current_page.click_button(edit_button)
    current_page = EditContactPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    current_page.complete_edit_contact(const.EDIT_FIRST_NAME,
                                       const.EDIT_LAST_NAME,
                                       const.EDIT_BIRTHDATE,
                                       const.EDIT_EMAIL_ADDRESS,
                                       const.EDIT_PHONE,
                                       const.EDIT_STREET1,
                                       const.EDIT_STREET2,
                                       const.EDIT_CITY,
                                       const.EDIT_STATE_PROVINCE,
                                       const.EDIT_POSTAL_CODE,
                                       const.EDIT_COUNTRY)
    current_page = ContactDetailsPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    assert current_page.find_element(first_name_field).text == "RICARDO"
    assert current_page.find_element(last_name_field).text == "DIAZ"
    assert current_page.find_element(birthdate_field).text == "1999-12-12"
    assert (current_page.find_element(email_address_field).text ==
            "hello@world.com")
    assert current_page.find_element(phone_field).text == "0987654321"
    assert (current_page.find_element(street1_field).text ==
            "BOULEVARD OF BROKEN DREAMS")
    assert current_page.find_element(street2_field).text == "80-180"
    assert current_page.find_element(city_field).text == "KYOTO"
    assert current_page.find_element(state_province_field).text == "HAMPSHIRE"
    assert current_page.find_element(postal_code_field).text == "200205"
    assert current_page.find_element(country_field).text == "FRANCE"
    logger.info("TEST 1: Executed")


@pytest.mark.edit_contact_with_empty_fields
def test_edit_contact_with_empty_fields(browser_contacts):
    """
    Test the editing of an existing contact
    with leaving the fields empty
    """
    logger.info("TEST 2: Start execution")
    current_page = ContactListPage(browser_contacts)
    current_page.open_contact()
    current_page = ContactDetailsPage(browser_contacts)
    current_page.click_button(edit_button)
    current_page = EditContactPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    (current_page.complete_edit_contact
     ("", "", "", "", "", "", "", "", "", "", ""))
    current_page = ContactDetailsPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("Validation failed: "
                                  "lastName: Path `lastName` is required., "
                                  "firstName: Path `firstName` is required.")
    logger.info("TEST 2: Executed")


@pytest.mark.edit_contact_with_invalid_characters
def test_edit_contact_with_invalid_characters(browser_contacts):
    """
    Test the editing of an existing contact
    with entering invalid type of characters
    to fields that do not accepts such characters
    """
    logger.info("TEST 3: Start execution")
    current_page = ContactListPage(browser_contacts)
    current_page.open_contact()
    current_page = ContactDetailsPage(browser_contacts)
    current_page.click_button(edit_button)
    current_page = EditContactPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    (current_page.
     complete_edit_contact(const.FIRST_NAME, const.LAST_NAME,
                           const.INVALID_CHARACTERS_BIRTHDATE,
                           const.INVALID_CHARACTERS_EMAIL_ADDRESS,
                           const.INVALID_CHARACTERS_PHONE,
                           const.STREET1, const.STREET2, const.CITY,
                           const.STATE_PROVINCE,
                           const.INVALID_CHARACTERS_POSTAL_CODE,
                           const.COUNTRY))
    current_page = ContactDetailsPage(browser_contacts)
    time.sleep(10)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert validation_message == ("Validation failed: "
                                  "postalCode: Postal code is invalid, "
                                  "phone: Phone number is invalid, "
                                  "email: Email is invalid, "
                                  "birthdate: Birthdate is invalid")
    logger.info("TEST 3: Executed")


@pytest.mark.edit_contact_with_max_amount_of_characters_exceeded
def test_edit_contact_with_max_amount_of_characters_exceeded(browser_contacts):
    """
    Test the editing of an existing contact
    with entering invalid type of characters
    to fields that do not accepts such characters
    """
    logger.info("TEST 4: Start execution")
    current_page = ContactListPage(browser_contacts)
    current_page.open_contact()
    current_page = ContactDetailsPage(browser_contacts)
    current_page.click_button(edit_button)
    current_page = EditContactPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    (current_page.
     complete_edit_contact(const.LONG_FIRST_NAME, const.LONG_LAST_NAME,
                           const.BIRTHDATE, const.EMAIL_ADDRESS,
                           const.LONG_PHONE,
                           const.LONG_STREET1, const.LONG_STREET2,
                           const.LONG_CITY, const.LONG_STATE_PROVINCE,
                           const.LONG_POSTAL_CODE, const.LONG_COUNTRY))
    current_page = ContactDetailsPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    validation_message = current_page.locate_validation_message()
    logger.info("VALIDATION MESSAGE: %s", validation_message)
    assert (validation_message ==
            ("Validation failed: country: Path `country` "
             "(`AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno`) "
             "is longer than the maximum allowed length (40)., "
             "postalCode: Path `postalCode` (`12345678901`) "
             "is longer than the maximum allowed length (10)., "
             "stateProvince: Path `stateProvince` "
             "(`Abcdefghijklmnopqrstu`) "
             "is longer than the maximum allowed length (20)., "
             "city: Path `city` "
             "(`AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno`) "
             "is longer than the maximum allowed length (40)., "
             "street2: Path `street2` "
             "(`AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno`) "
             "is longer than the maximum allowed length (40)., "
             "street1: Path `street1` "
             "(`AbcdefghijklmnopqrstuvwxyzAbcdefghijklmno`) "
             "is longer than the maximum allowed length (40)., "
             "phone: Path `phone` (`1234567890123456`) "
             "is longer than the maximum allowed length (15)., "
             "lastName: Path `lastName` (`Abcdefghijklmnopqrstu`) "
             "is longer than the maximum allowed length (20)., "
             "firstName: Path `firstName` (`Abcdefghijklmnopqrstu`) "
             "is longer than the maximum allowed length (20)."))
    logger.info("TEST 4: Executed")
