import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

class WorkPage(object):

    def __init__(self, url):
        self.url = url

    def GoogleSearch(self):
        driver_chrome = webdriver.Chrome()
        self.driver = driver_chrome
        driver_chrome.get(self.url)
        driver_chrome.maximize_window()
        time.sleep(3)

search = WorkPage('https://www.google.com')
search.GoogleSearch()
driver.close()