"""CONTACT DETAILS PAGE"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

edit_button = (By.ID, "edit-contact")
delete_button = (By.ID, "delete")

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


class ContactDetailsPage(BasePage):
    """Contact Details Page class"""
    def __init__(self, driver):
        """
        Initialize the ContactDetailsPage with a web driver.
        """
        super().__init__(driver)

    def click_edit_contact(self):
        """
        Click the edit button to edit the contact details.
        """
        edit_contact_element = self.find_element(edit_button)
        edit_contact_element.click()

    def click_delete_contact(self):
        """
        Click the delete button to delete the contact.
        """
        delete_contact_element = self.find_element(delete_button)
        delete_contact_element.click()

    def locate_first_name(self):
        """
        Locate the first name field.
        """
        return self.find_element(first_name_field)

    def locate_last_name(self):
        """
        Locate the last name field.
        """
        return self.find_element(last_name_field)

    def locate_birthdate(self):
        """
        Locate the birthdate field.
        """
        return self.find_element(birthdate_field)

    def locate_email_address(self):
        """
        Locate the email address field.
        """
        return self.find_element(email_address_field)

    def locate_phone(self):
        """
        Locate the phone field.
        """
        return self.find_element(phone_field)

    def locate_street1(self):
        """
        Locate the first line of the street address field.
        """
        return self.find_element(street1_field)

    def locate_street2(self):
        """
        Locate the second line of the street address field.
        """
        return self.find_element(street2_field)

    def locate_city(self):
        """
        Locate the city field.
        """
        return self.find_element(city_field)

    def locate_state_province(self):
        """
        Locate the state or province field.
        """
        return self.find_element(state_province_field)

    def locate_postal_code(self):
        """
        Locate the postal code field.
        """
        return self.find_element(postal_code_field)

    def locate_country(self):
        """
        Locate the country field.
        """
        return self.find_element(country_field)
