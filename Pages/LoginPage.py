from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage
from Config.config import TestData
from Locators.locators import Locators

class LoginPage(BasePage):

    """ This is the constructor class"""
    def __init__(self , driver):
        super().__init__(driver)

        self.driver.get(TestData.BASE_URL)

    """ Page actions """

    """get title of the page"""
    def get_login_page_title(self , title):
        return self.get_title(title)

    """Login to the web app"""
    def do_login(self , username , password):
        self.do_send_keys(Locators.EMAIL , username)
        self.do_send_keys(Locators.PASSWORD , password)


