"""PYTEST TEST CASES: CONTACTS"""

import time
import pytest
from pages.contact_list_page import ContactListPage
from pages.contact_details_page import ContactDetailsPage
from pages.edit_contact_page import EditContactPage
import test_data.constants as const
from logger.log_setup import logger


@pytest.mark.edit_contact
def test_edit_contact(browser_contacts):
    """
    Test the editing of an existing contact.
    """
    logger.info("TEST 2: Start execution")
    page_object = ContactListPage(browser_contacts)
    page_object.open_contact()
    page_object = ContactDetailsPage(browser_contacts)
    page_object.click_edit_contact()
    page_object = EditContactPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    page_object.complete_edit_contact(const.EDIT_FIRST_NAME,
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
    page_object = ContactDetailsPage(browser_contacts)
    time.sleep(1)  # This one is really needed!
    assert page_object.locate_first_name().text == "RICARDO"
    assert page_object.locate_last_name().text == "DIAZ"
    assert page_object.locate_birthdate().text == "1999-12-12"
    assert page_object.locate_email_address().text == "hello@world.com"
    assert page_object.locate_phone().text == "0987654321"
    assert page_object.locate_street1().text == "BOULEVARD OF BROKEN DREAMS"
    assert page_object.locate_street2().text == "80-180"
    assert page_object.locate_city().text == "KYOTO"
    assert page_object.locate_state_province().text == "HAMPSHIRE"
    assert page_object.locate_postal_code().text == "200205"
    assert page_object.locate_country().text == "FRANCE"
    logger.info("TEST 2: Executed")
