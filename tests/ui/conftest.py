"""PYTEST FIXTURE STORAGE"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import tests.test_data.constants as const
from log_test.log_setup import logger
# from pages.contact_details_page import ContactDetailsPage, delete_button
# from pages.contact_list_page import ContactListPage, logout_button
from pages.login_page import LoginPage


@pytest.fixture
def browser_contacts():
    """Fixture for testing contacts page."""
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-cache')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-blink-features=MetricsInterceptor')
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.get(const.URL_LANDING)
    current_page = LoginPage(chrome_browser)
    current_page.complete_login(const.EMAIL, const.PASSWORD)
    chrome_browser.implicitly_wait(10)

    yield chrome_browser
    chrome_browser.quit()


@pytest.fixture
def browser_sign_up_log_in():
    """Fixture for testing sign up and log in page."""
    logger.info("Fixture: Setting up started")
    options = Options()
    options.add_argument('--start-maximized')
    options.add_argument('--disable-cache')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--disable-blink-features=MetricsInterceptor')
    options.add_argument("--headless=new")
    options.add_argument('--no-sandbox')
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    chrome_browser.get(const.URL_LANDING)

    yield chrome_browser
    chrome_browser.quit()

# @pytest.fixture
# def general_fixture():
#     """
#     General fixture.
#     Set up: Login.
#     Tear down: Logout.
#     """
#     log_test.info("Fixture: Setting up started")
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-search-engine-choice-screen")
#     chrome_browser = webdriver.Chrome(options=chrome_options)
#     chrome_options.add_argument('--headless=new')
#     chrome_browser.implicitly_wait(5)
#     chrome_browser.get(const.URL_LANDING)
#     current_page = LoginPage(chrome_browser)
#     current_page.complete_login(const.EMAIL, const.PASSWORD)
#     yield chrome_browser
#     chrome_browser.get(const.URL_CONTACTS)
#     current_page = ContactListPage(chrome_browser)
#     current_page.click_button(logout_button)
#     chrome_browser.quit()
#     print("")
#
#
# @pytest.fixture
# def browser_sign_up_log_in():
#     """
#     Fixture for testing sign up and log in page.
#     Set up: No actions.
#     Tear down: Logout.
#     """
#     log_test.info("Fixture: Setting up started")
#     chrome_options = Options()
#     # chrome_options.add_argument("--disable-search-engine-choice-screen")
#     chrome_browser = webdriver.Chrome(options=chrome_options)
#     chrome_options.add_argument('--headless=new')
#     chrome_browser.implicitly_wait(5)
#     chrome_browser.get(const.URL_LANDING)
#     yield chrome_browser
#     chrome_browser.get(const.URL_CONTACTS)
#     current_page = ContactListPage(chrome_browser)
#     current_page.click_button(logout_button)
#     chrome_browser.quit()
#
#
# @pytest.fixture
# def browser_contacts():
#     """
#     Fixture for testing contacts page.
#     Set up: Log in.
#     Tear down: Delete contact in case it was created during the tests.
#     """
#     log_test.info("Fixture: Setting up started")
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-search-engine-choice-screen")
#     chrome_browser = webdriver.Chrome(options=chrome_options)
#     chrome_options.add_argument('--headless=new')
#     chrome_browser.implicitly_wait(5)
#     chrome_browser.get(const.URL_LANDING)
#     log_test.debug("Fixture: Logging in")
#     current_page = LoginPage(chrome_browser)
#     current_page.complete_login(const.EMAIL, const.PASSWORD)
#     current_page = ContactListPage(chrome_browser)
#     contact_count_before_yield = len(current_page.locate_contact_rows())
#     log_test.debug("Fixture: Yielding browser control to the tests file")
#     yield chrome_browser
#     chrome_browser.get(const.URL_CONTACTS)
#     current_page = ContactListPage(chrome_browser)
#     contact_count_after_yield = len(current_page.locate_contact_rows())
#     log_test.debug("Fixture: Deletting Contact (on demand)")
#     if contact_count_after_yield > contact_count_before_yield:
#         current_page.open_contact()
#         current_page = ContactDetailsPage(chrome_browser)
#         current_page.click_button(delete_button)
#         time.sleep(1)
#         alert = chrome_browser.switch_to.alert
#         time.sleep(1)
#         alert.accept()
#     chrome_browser.quit()
