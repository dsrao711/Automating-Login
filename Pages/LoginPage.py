from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage

class LoginPage(BasePage):

    """ Locators """
    EMAIL = (By.ID , "txtUserName")
    PASSWORD = (By.ID , "txtPassword")
    BUTTON_LOGIN = (By.CSS_SELECTOR , "btn.btn-primary.shadow-2.mb-4")

    """ This is the constructor class"""
    def __init__(self , driver):
        super().__init__(driver)

    """ Page actions """

    """get title of the page"""
    def get_login_page_title(self , title):
        return self.get_title(title)

    """Login to the web app"""
    def do_login(self , username , password):
        self.do_send_keys(self.EMAIL , username)
        self.do_send_keys(self.PASSWORD , password)


