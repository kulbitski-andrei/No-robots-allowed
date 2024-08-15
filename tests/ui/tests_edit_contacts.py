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
    logger.info("TEST 2: Start execution")
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
    assert current_page.find_element(email_address_field).text == "hello@world.com"
    assert current_page.find_element(phone_field).text == "0987654321"
    assert current_page.find_element(street1_field).text == "BOULEVARD OF BROKEN DREAMS"
    assert current_page.find_element(street2_field).text == "80-180"
    assert current_page.find_element(city_field).text == "KYOTO"
    assert current_page.find_element(state_province_field).text == "HAMPSHIRE"
    assert current_page.find_element(postal_code_field).text == "200205"
    assert current_page.find_element(country_field).text == "FRANCE"
    logger.info("TEST 2: Executed")
