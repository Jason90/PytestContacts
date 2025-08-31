from core.page.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from config import Web_Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class HomePage(BasePage):

    LOCATOR_LNK_LOGIN = (By.ID, 'menu-item-98557')
    
    def __init__(self, driver):
        super().__init__(driver, Web_Config.WEB_BASE_URL) 
        self.__lnk_login=None
    
    @property
    def lnk_login(self):
        if self.__lnk_login==None:
            self.__lnk_login=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.LOCATOR_LNK_LOGIN))
            
        return self.__lnk_login