"""LOGIN PAGE"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

email_field = (By.ID, "email")
password_field = (By.ID, "password")
submit_button = (By.ID, "submit")
signup_button = (By.ID, "signup")
validation_message_field = (By.ID, "error")


class LoginPage(BasePage):
    """Login Page class"""

    def __init__(self, driver):
        """
        Initialize the LoginPage with a web driver.
        """
        super().__init__(driver)

    def complete_login(self, email, password):
        """
        Complete the login process by entering the email
        and password and submitting the form.
        """
        self.enter_text(email, email_field)
        self.enter_text(password, password_field)
        self.click_button(submit_button)

    def locate_validation_message(self):
        """
        Finds validation message on the page.
        """
        validation_message = self.find_element(validation_message_field)
        text = validation_message.text
        return text
