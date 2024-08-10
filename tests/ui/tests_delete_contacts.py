"""PYTEST TEST CASES: CONTACTS"""

import pytest
from pages.contact_list_page import ContactListPage
from pages.contact_details_page import ContactDetailsPage
from logger.log_setup import logger


@pytest.mark.delete_contact
def test_delete_contact(browser_contacts):
    """
    Test the deletion of an existing contact.
    """
    logger.info("TEST 3: Start execution")
    page_object = ContactListPage(browser_contacts)
    contact_count_before_delete = len(page_object.locate_contact_rows())
    logger.info("Contact count: %s", contact_count_before_delete)
    page_object.open_contact()
    page_object = ContactDetailsPage(browser_contacts)
    page_object.click_delete_contact()
    alert = browser_contacts.switch_to.alert
    alert.accept()
    page_object = ContactListPage(browser_contacts)
    contact_count_after_delete = len(page_object.locate_contact_rows())
    logger.info("Contact count: %s", contact_count_after_delete)
    assert contact_count_before_delete - contact_count_after_delete == 1
    logger.info("TEST 3: Executed")
