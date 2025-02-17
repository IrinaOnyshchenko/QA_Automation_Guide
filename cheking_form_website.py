from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import  Keys
from selenium.webdriver.chrome.service import Service
import time

#Ініціалізація вебрайвера
s=Service('/Users/irinaonyshch23/Downloads/chromedriver-mac-arm64/chromedriver')
driver = webdriver.Chrome(service=s)

#Відкриваєм вебсайт
website = driver.get("https://allright.com/uk/dashboard")
time.sleep(3)

#Знаходимо пошукову строку та вводимо запит
serch_field = driver.find_element(By.ID, "ember15")
serch_field.send_keys("irinaonyshchenko23@gmail.com")

time.sleep(2)

print (driver.title)

assert "школа" in driver.title
assert driver.title=="Онлайн школа англійської мови для дітей All Right"
