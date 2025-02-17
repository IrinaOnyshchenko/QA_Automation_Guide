import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def driver():
    service = Service('/Users/irinaonyshch23/Downloads/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()