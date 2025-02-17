import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

#Ініціалізація вебрайвера
s=Service('/Users/irinaonyshch23/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=s)
@pytest.fixture

def driver ():
    #створюємо та налагоджуємо драйвер
    driver = webdriver.Chrome(service=s)
    driver.get("https://allright.com/uk/login")
    yield driver #передаємо об'єкт драйвера до тесту
    driver.quit()

def test_registration(driver):
    #заповнюємо форму реєстрації
    serch_field = driver.find_element(By.ID, "ember15")
    serch_field.send_keys("irinaonyshchenko23@gmail.com")
    receive_code = driver.find_element(By.XPATH, '/html/body/div[5]/div/div[1]/div[2]/div[1]/form/button').click()
    time.sleep(5)
    success_message = driver.find_element(By.XPATH, "//*[@id='ember18']")







