"""PYTEST FIXTURE STORAGE"""

import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import test_data.constants as const
from logger.log_setup import logger
from pages.contact_details_page import ContactDetailsPage
from pages.contact_list_page import ContactListPage
from pages.login_page import LoginPage


@pytest.fixture
def general_fixture():
    """
    General fixture:
    Set up: Login.
    Tear down: Logout.
    """
    logger.info("Fixture: Setting up started")
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(5)
    chrome_browser.get(const.URL_LANDING)
    page_object = LoginPage(chrome_browser)
    page_object.complete_login(const.EMAIL, const.PASSWORD)
    yield chrome_browser
    chrome_browser.get(const.URL_CONTACTS)
    page_object = ContactListPage(chrome_browser)
    page_object.logout()
    chrome_browser.quit()


@pytest.fixture
def browser_sign_up_log_in():
    """
    Fixture for testing sign up and log in page.
    Set up: No actions.
    Tear down: Logout.
    """
    logger.info("Fixture: Setting up started")
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(5)
    chrome_browser.get(const.URL_LANDING)
    yield chrome_browser
    chrome_browser.get(const.URL_CONTACTS)
    page_object = ContactListPage(chrome_browser)
    page_object.logout()
    chrome_browser.quit()


@pytest.fixture
def browser_contacts():
    """
    Fixture for testing contacts page.
    Set up: Log in.
    Tear down: Delete contact in case it was created during the test.
    """
    logger.info("Fixture: Setting up started")
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(5)
    chrome_browser.get(const.URL_LANDING)
    logger.debug("Fixture: Logging in")
    page_object = LoginPage(chrome_browser)
    page_object.complete_login(const.EMAIL, const.PASSWORD)
    page_object = ContactListPage(chrome_browser)
    contact_count_before_yield = len(page_object.locate_contact_rows())
    logger.debug("Fixture: Yielding browser control to the test file")
    yield chrome_browser
    chrome_browser.get(const.URL_CONTACTS)
    page_object = ContactListPage(chrome_browser)
    contact_count_after_yield = len(page_object.locate_contact_rows())
    logger.debug("Fixture: Deletting Contact (on demand)")
    if contact_count_after_yield > contact_count_before_yield:
        page_object.open_contact()
        page_object = ContactDetailsPage(chrome_browser)
        page_object.click_delete_contact()
        time.sleep(1)
        alert = chrome_browser.switch_to.alert
        time.sleep(1)
        alert.accept()
    chrome_browser.quit()
