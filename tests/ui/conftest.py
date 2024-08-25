"""PYTEST FIXTURE STORAGE"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import test_data.constants as const
from test_data.service_methods import add_arguments
from log_test.log_setup import logger
from pages.login_page import LoginPage


@pytest.fixture
def browser_contacts():
    """Fixture for testing contacts page."""
    options = Options()
    options = add_arguments(options)
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
    options = add_arguments(options)
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    chrome_browser.get(const.URL_LANDING)

    yield chrome_browser
    chrome_browser.quit()
