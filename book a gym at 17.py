from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

#tell the computer where the chrome driver is
PATH = "D:\Coding_Tools\Python\chromedriver.exe"
driver = webdriver.Chrome(PATH)

#open gym booking website
driver.get("https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK")

#find the 17:00 row and click on book
gym_17 = driver.find_element_by_link_text("Book")
gym_17.click()
time.sleep(3)
accept_cookie = driver.find_element_by_id("onetrust-accept-btn-handler")
accept_cookie.click()


#go to the 'proceed with booking' page and input username then clcik proceed
input_username = driver.find_element_by_xpath("//*[@id=\"single-column-content\"]/div/div/div/div[2]/div/form/input[4]")
input_username.send_keys("21200198")
time.sleep(1)
proceed = driver.find_element_by_xpath("//*[@id=\"single-column-content\"]/div/div/div/div[2]/div/form/input[5]")
proceed.click()

#go to the confirm booking page and click confirm booking
time.sleep(2)
confirm = driver.find_element_by_link_text("Confirm Booking")
confirm.click()
time.sleep(2)
print("Booking Successful!")

driver.quit()


#-------------------If you want more function, see eferences below-----------------#
#clcik on date selection menu
'''
date_selection = driver.find_element_by_name("p_code1")
date_selection.click()
'''
#find all the dates and click the third one
'''
wanted_date = driver.find_elements_by_tag_name("option")
wanted_date[2].click()
'''
#click on fresh button
'''
fresh = driver.find_element_by_link_text("Refresh")
fresh.click()
'''