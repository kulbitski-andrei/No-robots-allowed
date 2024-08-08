"""CONTACT LIST PAGE"""

from selenium.webdriver.common.by import By
from pages.base_page import BasePage

add_contact_button = (By.ID, "add-contact")
contact_row = (By.XPATH, "//tr[@class=\"contactTableBodyRow\"][1]")
contact_row_list = (By.XPATH, "//tr[@class=\"contactTableBodyRow\"]")


class ContactListPage(BasePage):
    """Contact List Page class"""

    def __init__(self, driver):
        """
        Initialize the ContactListPage with a web driver.
        """
        super().__init__(driver)

    def click_add_contact(self):
        """
        Click the add contact button to navigate to the add contact page.
        """
        add_contact_element = self.find_element(add_contact_button)
        add_contact_element.click()

    def open_contact(self):
        """
        Click the first contact row to open the contact details.
        """
        open_contact = self.find_element(contact_row)
        open_contact.click()

    def locate_contact_row(self):
        """
        Locate the first contact row in the contact list.
        """
        return self.find_element(contact_row)

    def locate_contact_rows(self):
        """
        Locate multiple contact rows.
        """
        list_of_rows = self.find_elements(*contact_row_list)
        return list_of_rows
