from selenium.webdriver.common.by import By

class Locators :

    EMAIL = (By.ID, "txtUserName")
    PASSWORD = (By.ID, "txtPassword")
    BUTTON_LOGIN = (By.CSS_SELECTOR, "btn.btn-primary.shadow-2.mb-4")