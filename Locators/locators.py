from selenium.webdriver.common.by import By

class Locators :

    """
     This has to be changed according to the web application
     Inspect the HTML page and change the id's/name/css selector accordingly
    """

    EMAIL = (By.ID, "txtUserName")
    PASSWORD = (By.ID, "txtPassword")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "btn.btn-primary.shadow-2.mb-4")