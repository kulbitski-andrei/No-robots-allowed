"""PYTEST TEST CASES: CONTACTS"""

import pytest
from pages.contact_list_page import ContactListPage
from logger.log_setup import logger


@pytest.mark.create_new_contact
def test_create_new_contact(browser_contacts):
    """
    Test the creation of a new contact.
    """
    logger.info("TEST 1: Start execution")
    page_object = ContactListPage(browser_contacts)
    assert page_object.locate_contact_row() is not None
    logger.info("TEST 1: Executed")
