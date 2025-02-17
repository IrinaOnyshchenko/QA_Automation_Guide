from selenium import webdriver
from selenium.webdriver.common.by import By

class FacebookLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.facebook.com/?locale=ru_RU"
        self.input_email = (By.ID, "email")
        self.input_password = (By.ID, "pass")
        self.button_login = (By.NAME, "login")

    def open(self):
        self.driver.get(self.url)

    def enter_email(self, email):
        self.driver.find_element(*self.input_email).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.input_password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.button_login).click()