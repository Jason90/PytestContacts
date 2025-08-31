from core.page.base import BasePage
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from config import Web_Config
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class LoginPage(BasePage):

    LOCATOR_TXT_USERNAME = (By.ID, 'username')
    LOCATOR_TXT_PASSWORD = (By.ID, 'password')
    LOCATOR_BTN_LOGIN= (By.ID, 'proceed')
    LOCATOR_LBL_MESSAGE= (By.ID, 'messageContainer')
    
    def __init__(self, driver):
        super().__init__(driver, Web_Config.WEB_LOGIN_URL) 
        self.__txt_username=None
        self.__txt_password=None
        self.__btn_login=None
        self.__lbl_message=None
    
    @property
    def txt_username(self):
        if self.__txt_username is None:
            self.__txt_username=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.LOCATOR_TXT_USERNAME))
            
        return self.__txt_username
    
    @txt_username.setter
    def txt_username(self,value):
        self.txt_username.clear()
        self.txt_username.send_keys(value)

    @property
    def txt_password(self):
        if self.__txt_password is None:
            self.__txt_password=WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.LOCATOR_TXT_PASSWORD))
            
        return self.__txt_password
    
    @txt_password.setter
    def txt_password(self,value):
        self.txt_password.clear()
        self.txt_password.send_keys(value)
    
    @property
    def btn_login(self):
        if self.__btn_login is None:
            self.__btn_login=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.LOCATOR_BTN_LOGIN))
            
        return self.__btn_login 
    
    
    @property
    def lbl_message(self):
        if self.__lbl_message is None:
            self.__lbl_message=WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.LOCATOR_LBL_MESSAGE))
            
        return self.__lbl_message 
