"""PYTEST TEST CASES: CONTACTS"""

import pytest
from pages.contact_list_page import ContactListPage
from pages.contact_details_page import ContactDetailsPage, delete_button
from logger.log_setup import logger


@pytest.mark.delete_contact
def test_delete_contact(browser_contacts):
    """
    Test the deletion of an existing contact.
    """
    logger.info("TEST 3: Start execution")
    current_page = ContactListPage(browser_contacts)
    contact_count_before_delete = len(current_page.locate_contact_rows())
    logger.info("Contact count: %s", contact_count_before_delete)
    current_page.open_contact()
    current_page = ContactDetailsPage(browser_contacts)
    current_page.click_button(delete_button)
    alert = browser_contacts.switch_to.alert
    alert.accept()
    current_page = ContactListPage(browser_contacts)
    contact_count_after_delete = len(current_page.locate_contact_rows())
    logger.info("Contact count: %s", contact_count_after_delete)
    assert contact_count_before_delete - contact_count_after_delete == 1
    logger.info("TEST 3: Executed")
