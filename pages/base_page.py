"""BASE PAGE"""

from selenium.webdriver.common.by import By

logout_button = (By.ID, "logout")


class BasePage:
    """Base Page class"""

    def __init__(self, driver):
        """
        Initialize the BasePage with a web driver.
        """
        self.driver = driver

    def open(self, url):
        """
        Open a web page with the given URL.
        """
        self.driver.get(url)

    def enter_text(self, text, field):
        """
        Enter the text into the field.
        """
        input_var = self.find_element(field)
        input_var.send_keys(text)

    def click_button(self, button):
        """
        Click the submit button to submit the form.
        """
        button_var = self.find_element(button)
        button_var.click()

    def find_element(self, selector):
        """
        Find a web element using the given selector.
        """
        return self.driver.find_element(*selector)

    def find_elements(self, *selectors):
        """
        Find a web element using the given selector.
        """
        return self.driver.find_elements(*selectors)
