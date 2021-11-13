from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import  expected_conditions as EC

""" This class is the parent of all pages """

class BasePage:

    def __init__(self , driver):
        self.driver = driver

    """ Clicking a button """
    def do_click(self , by_locator):
        WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located(by_locator)).click()

    """ Sending input to forms """
    def do_send_keys(self , by_locator , text):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """ Getting text from element """
    def get_element_text(self , by_locator):
        element = WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """ To check if an element is present """
    def is_enabled(self , by_locator):
        element = WebDriverWait(self.driver , 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """ Getting the title """
    def get_title(self , title):
        WebDriverWait(self.driver,10).until(EC.title_is(title))
        return self.driver.title