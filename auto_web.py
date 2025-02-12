import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time

s=Service('/Users/irinaonyshch23/Downloads/chromedriver')
driver = webdriver.Chrome(service=s)

driver.get("https://www.adidas.ua/")
time.sleep(3)


