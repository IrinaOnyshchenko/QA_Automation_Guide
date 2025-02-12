import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver import ActionChains


#initialize webdriver
driver = webdriver.Firefox()

#open URL & maximize window
driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()
time.sleep(5)

#scrolling to laptop
laptop = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/h4/a')
laptop.location_once_scrolled_into_view
time.sleep(3)

laptop_button = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[1]/div/div[2]/h4/a')
laptop_button.click()
time.sleep(3)

add_to_cart = driver.find_element(By.XPATH, '//*[@id="button-cart"]')
add_to_cart.click()
time.sleep(3)

proceed_with_cart = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/div/button')
proceed_with_cart.click()
time.sleep(3)

checkout_cart = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/div/ul/li[2]/div/p/a[2]/strong')
checkout_cart.click()
time.sleep(3)

registration = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/label')
registration.click()
time.sleep(3)

reg_continue = driver.find_element(By.XPATH, '//*[@id="button-account"]')
reg_continue.click()
time.sleep(3)


driver.close()