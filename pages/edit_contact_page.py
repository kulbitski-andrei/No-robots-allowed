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

    def edit_first_name(self, first_name):
        """
        Edit the first name field.
        """
        first_name_input = self.find_element(first_name_field)
        first_name_input.clear()
        first_name_input.send_keys(first_name)

    def edit_last_name(self, last_name):
        """
        Edit the last name field.
        """
        last_name_input = self.find_element(last_name_field)
        last_name_input.clear()
        last_name_input.send_keys(last_name)

    def edit_birthdate(self, birthdate):
        """
        Edit the birthdate field.
        """
        birthdate_input = self.find_element(birthdate_field)
        birthdate_input.clear()
        birthdate_input.send_keys(birthdate)

    def edit_email_address(self, email_address):
        """
        Edit the email address field.
        """
        email_address_input = self.find_element(email_address_field)
        email_address_input.clear()
        email_address_input.send_keys(email_address)

    def edit_phone(self, phone):
        """
        Edit the phone field.
        """
        phone_input = self.find_element(phone_field)
        phone_input.clear()
        phone_input.send_keys(phone)

    def edit_street1(self, street1):
        """
        Edit the first line of the street address field.
        """
        street1_input = self.find_element(street1_field)
        street1_input.clear()
        street1_input.send_keys(street1)

    def edit_street2(self, street2):
        """
        Edit the second line of the street address field.
        """
        street2_input = self.find_element(street2_field)
        street2_input.clear()
        street2_input.send_keys(street2)

    def edit_city(self, city):
        """
        Edit the city field.
        """
        city_input = self.find_element(city_field)
        city_input.clear()
        city_input.send_keys(city)

    def edit_state_province(self, state_province):
        """
        Edit the state or province field.
        """
        state_province_input = self.find_element(state_province_field)
        state_province_input.clear()
        state_province_input.send_keys(state_province)

    def edit_postal_code(self, postal_code):
        """
        Edit the postal code field.
        """
        postal_code_input = self.find_element(postal_code_field)
        postal_code_input.clear()
        postal_code_input.send_keys(postal_code)

    def edit_country(self, country):
        """
        Edit the country field.
        """
        country_input = self.find_element(country_field)
        country_input.clear()
        country_input.send_keys(country)

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
        self.edit_first_name(first_name)
        self.edit_last_name(last_name)
        self.edit_birthdate(birthdate)
        self.edit_email_address(email_address)
        self.edit_phone(phone)
        self.edit_street1(street1)
        self.edit_street2(street2)
        self.edit_city(city)
        self.edit_state_province(state_province)
        self.edit_postal_code(postal_code)
        self.edit_country(country)
        self.click_submit()
