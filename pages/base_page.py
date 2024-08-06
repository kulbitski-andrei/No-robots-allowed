"""BASE PAGE"""


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

    def find_element(self, selector):
        """
        Find a web element using the given selector.
        """
        return self.driver.find_element(*selector)
