from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver: WebDriver, url):
        self.driver = driver
        self.url = url
        self._element_cache = {}

    def navigate(self,url):
        self.driver.get(url)
    
    def navigate(self):
        self.driver.get(self.url)
    
    def find_element(self, locator) :
        if locator not in self._element_cache:
            self._element_cache[locator] = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))
        return self._element_cache[locator]
    
    def find_elements(self, locator):
        return self.driver.find_elements(locator)

    def input_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def click_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(locator))
            element.click()

        except ElementClickInterceptedException:
            self.driver.execute_script("arguments[0].click()", element)
    
    def lost_focus(self, locator):
        element = self.find_element(locator)
        element.send_keys(Keys.TAB)
        
