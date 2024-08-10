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

    def enter_email(self, email):
        """
        Enter the email address into the email field.
        """
        email_input = self.find_element(email_field)
        email_input.send_keys(email)

    def enter_password(self, password):
        """
        Enter the password into the password field.
        """
        password_input = self.find_element(password_field)
        password_input.send_keys(password)

    def click_submit(self):
        """
        Click the submit button to log in.
        """
        submit_element = self.find_element(submit_button)
        submit_element.click()

    def complete_login(self, email, password):
        """
        Complete the login process by entering the email
        and password and submitting the form.
        """
        self.enter_email(email)
        self.enter_password(password)
        self.click_submit()

    def locate_validation_message(self):
        """
        Finds validation message on the page.
        """
        validation_message = self.find_element(validation_message_field)
        text = validation_message.text
        return text

    def click_sign_up(self):
        """
        Click the sign up button to open sign up page.
        """
        signup_element = self.find_element(signup_button)
        signup_element.click()
