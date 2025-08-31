from biz.web import EBPortal
import pytest
from config import Web_Config
import biz.web

@pytest.mark.parametrize("username,password",
    [
        # ("Valid User","Valid Password"),
        ("Invalid User","Invalid Password"),
        ("Valid User","Invalid Password"),
    ]
)
def test_login(username,password):
    # biz.web.page.pg_home.navigate()
    
    eb=EBPortal()
    eb.pg_home.navigate()
    eb.pg_home.lnk_login.click()
    
    eb.pg_login.txt_username=username
    eb.pg_login.txt_password=password
    
    eb.pg_login.btn_login.click()
    
    assert Web_Config.WEB_LOGIN_URL in eb.pg_login.driver.current_url,"Page has navigated away from the login page"
    assert eb.pg_login.lbl_message.text in ("Your login attempt was not successful. Please try again." ,"Your account has been locked.\nContact your administrator or unlock your account.")
    