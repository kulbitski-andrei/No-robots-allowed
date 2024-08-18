"""EDIT CONTACT PAGE"""

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


class EditContactPage(BasePage):
    """Edit Contact Page class"""

    def __init__(self, driver):
        """
        Initialize the EditContactPage with a web driver.
        """
        super().__init__(driver)

    def edit_text(self, text, field):
        """
        Edit the text into the field.
        """
        input_var = self.find_element(field)
        input_var.clear()
        input_var.send_keys(text)

    def edit_first_name(self, first_name):
        """
        Edit the first name field.
        """
        first_name_input = self.find_element(first_name_field)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def click_submit(self):
        """
        Click the submit button to submit the edited contact details.
        """
        submit_form_button = self.find_element(submit_button)
        submit_form_button.click()

    def complete_edit_contact(self, first_name, last_name, birthdate,
                              email_address, phone, street1, street2, city,
                              state_province, postal_code, country):
        """
        Complete the process of editing a contact
        by filling out the form and submitting it.
        """
        self.edit_text(first_name, first_name_field)
        self.edit_text(last_name, last_name_field)
        self.edit_text(birthdate, birthdate_field)
        self.edit_text(email_address, email_address_field)
        self.edit_text(phone, phone_field)
        self.edit_text(street1, street1_field)
        self.edit_text(street2, street2_field)
        self.edit_text(city, city_field)
        self.edit_text(state_province, state_province_field)
        self.edit_text(postal_code, postal_code_field)
        self.edit_text(country, country_field)
        self.click_submit()
