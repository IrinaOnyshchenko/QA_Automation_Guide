import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver import ActionChains


#initialize webdriver
driver = webdriver.Chrome('/Users/irinaonyshch23/Downloads/chromedriver-mac-arm64/chromedriver')

#open URL & maximize window
driver.get('https://tutorialsninja.com/demo/')
driver.maximize_window()
time.sleep(3)

#Phones button
phones = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div[2]/ul/li[6]/a')
phones.click()
time.sleep(3)

#iphone
iphone = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div[2]/div/div[2]/div[1]/h4/a')
iphone.click()
time.sleep(3)

#inspecting photos
first_photo = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div[1]/ul[1]/li[1]/a/img')
first_photo.click()
time.sleep(2)

#next picture
next_photo = driver.find_element(By.XPATH, '/html/body/div[2]/div/button[2]')

for i in range(0,5):
    next_photo.click()
    time.sleep(2)

#screenshot
driver.save_screenshot('screenshot#' + str(random.randint(0,101)) + '.png')

#closing photos
close_photo = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/button')
close_photo.click()
time.sleep(2)

#changing quantity in cart
change_qnt  =driver.find_element(By.XPATH, '//*[@id="input-quantity"]')
change_qnt.click()
time.sleep(2)

change_qnt.clear()
time.sleep(2)
change_qnt.send_keys('2')
time.sleep(2)

#adding to cart
add_cart = driver.find_element(By.XPATH, '//*[@id="button-cart"]')
add_cart.click()
time.sleep(2)

#finding laptop without clicking
find_laptop = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div[2]/ul/li[2]/a')
action = ActionChains(driver)
action.move_to_element(find_laptop).perform()
time.sleep(2)

#clicking on laptop menu

laptop = driver.find_element(By.XPATH, '/html/body/div[1]/nav/div[2]/ul/li[2]/div/a')
laptop.click()
time.sleep(5)

#choosing laptop
choose_lap = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[4]/div[1]/div/div[2]/div[1]/h4/a')
choose_lap.click()
time.sleep(3)

#scrolling tp add to cart button
add_laptop = driver.find_element(By.ID, 'button-cart')
add_laptop.location_once_scrolled_into_view
time.sleep(2)

#work with calendar for choosing data of delivery
buy_laptop = driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div/div[2]/div[2]/div[1]/div/span/button/i')
buy_laptop.click()
time.sleep(2)

next_click = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/table/thead/tr[1]/th[3]')
find_data = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[1]/table/thead/tr[1]/th[2]")

while find_data.text!= "December 2022":
    next_click.click()
time.sleep(3)

#day 31 2022 De ember
calendar_date = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[1]/table/tbody/tr[5]/td[6]')
calendar_date.click()
time.sleep(2)
add_laptop.click()
time.sleep(2)

#g0 to cart
go_to_cart = driver.find_element(By.XPATH, '//*[@id="cart-total"]')
go_to_cart.click()
time.sleep(2)

#cheking out to proceed
check_out = driver.find_element(By.XPATH, '/html/body/header/div/div/div[3]/div/ul/li[2]/div/p/a[2]/strong')
check_out.click()
time.sleep(4)

driver.close()


