import pytest
from facebook_login_page import FacebookLoginPage

def test_facebook_login(driver):
    page = FacebookLoginPage(driver)
    page.open()
    page.enter_email('irinaonyshchenko23@gmail.com')
    page.enter_password('Myfacebook23')
    page.click_login()

    assert "Facebook" in driver.title