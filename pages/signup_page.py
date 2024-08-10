"""SIGNUP PAGE"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

first_name_field = (By.ID, "firstName")
last_name_field = (By.ID, "lastName")
email_field = (By.ID, "email")
password_field = (By.ID, "password")
submit_button = (By.ID, "submit")
validation_message_field = (By.ID, "error")

class SignupPage(BasePage):
    """Signup Page class"""

    def __init__(self, driver):
        """
        Initialize the SignupPage with a web driver.
        """
        super().__init__(driver)

    def enter_first_name(self, first_name):
        """
        Enter the first name into the first name field.
        """
        first_name_input = self.find_element(first_name_field)
        first_name_input.send_keys(first_name)

    def enter_last_name(self, last_name):
        """
        Enter the last name into the last name field.
        """
        last_name_input = self.find_element(last_name_field)
        last_name_input.send_keys(last_name)

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

    def complete_signup(self, first_name, last_name, email, password):
        """
        Complete the sign up process by entering the name,
        email and password and submitting the form.
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_email(email)
        self.enter_password(password)

    def locate_validation_message(self):
        """
        Finds validation message on the page.
        """
        validation_message = self.find_element(validation_message_field)
        text = validation_message.text
        return text
