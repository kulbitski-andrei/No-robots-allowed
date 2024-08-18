"""ADD CONTACT PAGE"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

first_name_field = (By.ID, "firstName")
last_name_field = (By.ID, "lastName")
birthdate_field = (By.ID, "birthdate")
email_address_field = (By.ID, "email")
phone_field = (By.ID, "phone")
street1_field = (By.ID, "street1")
street2_field = (By.ID, "street2")
city_field = (By.ID, "city")
state_province_field = (By.ID, "stateProvince")
postal_code_field = (By.ID, "postalCode")
country_field = (By.ID, "country")
submit_button = (By.ID, "submit")
validation_message_field = (By.ID, "error")


class AddContactPage(BasePage):
    """Add Contact Page class"""
    def __init__(self, driver):
        """
        Initialize the AddContactPage with a web driver.
        """
        super().__init__(driver)

    def click_submit(self):
        """
        Click the submit button to submit the form.
        """
        submit_form_button = self.find_element(submit_button)
        submit_form_button.click()

    def complete_add_new_contact(self, first_name, last_name, birthdate,
                                 email_address, phone, street1, street2,
                                 city, state_province, postal_code, country):
        """
        Complete the process of adding a new contact
        by filling out the form and submitting it.
        """
        self.enter_text(first_name, first_name_field)
        self.enter_text(last_name, last_name_field)
        self.enter_text(birthdate, birthdate_field)
        self.enter_text(email_address, email_address_field)
        self.enter_text(phone, phone_field)
        self.enter_text(street1, street1_field)
        self.enter_text(street2, street2_field)
        self.enter_text(city, city_field)
        self.enter_text(state_province, state_province_field)
        self.enter_text(postal_code, postal_code_field)
        self.enter_text(country, country_field)
        self.click_button(submit_button)

    def locate_validation_message(self):
        """
        Finds validation message on the page.
        """
        validation_message = self.find_element(validation_message_field)
        text = validation_message.text
        return text
