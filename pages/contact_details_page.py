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
validation_message_field = (By.ID, "error")


class ContactDetailsPage(BasePage):
    """Contact Details Page class"""

    def __init__(self, driver):
        """
        Initialize the ContactDetailsPage with a web driver.
        """
        super().__init__(driver)

    def locate_validation_message(self):
        """
        Finds validation message on the page.
        """
        validation_message = self.find_element(validation_message_field)
        text = validation_message.text
        return text
