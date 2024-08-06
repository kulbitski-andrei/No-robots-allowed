"""PYTEST FIXTURE STORAGE"""

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import test_data.constants as const
from logger.log_setup import logger


@pytest.fixture
def browser():
    """
    Fixture to set up and tear down the browser instance for each test.
    """
    logger.info("Setting up browser ...")
    chrome_options = Options()
    chrome_options.add_argument("--disable-search-engine-choice-screen")
    chrome_browser = webdriver.Chrome(options=chrome_options)
    chrome_browser.implicitly_wait(5)
    chrome_browser.get(const.URL)
    yield chrome_browser
    chrome_browser.quit()
