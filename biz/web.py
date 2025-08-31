from selenium import webdriver
from core.page.home import HomePage
from core.page.login import LoginPage

class EBPortal():
    def __init__(self) -> None:
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        
        self.pg_home = HomePage(self.driver)
        self.pg_login = LoginPage(self.driver)
        
    def __del__(self):
        self.driver.quit()
        
    def login(self,user,password):
        self.pg_home.navigate()
        self.pg_home.lnk_login.click()
        
        self.pg_login.txt_username.text="Jason"
        self.pg_login.txt_password.text="password"
        self.pg_login.btn_login.click()