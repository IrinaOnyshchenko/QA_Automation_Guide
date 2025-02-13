import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

s=Service('/Users/irinaonyshch23/Downloads/chromedriver')
driver = webdriver.Chrome(service=s)
driver.get('https://uk-ua.facebook.com/')
time.sleep(3)
driver.find_element(By.ID, 'email').send_keys('iryna')
time.sleep(3)
driver.find_element(By.NAME, 'pass').send_keys('mypass')
time.sleep(3)
driver.find_element(By.NAME, 'login').submit()
time.sleep(3)
driver.close()
