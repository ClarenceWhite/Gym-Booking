#This program is only for booking gym slot at 17:00, you can change the way it runs as you want.
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import time
import datetime

#time range
d_time = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:00', '%Y-%m-%d%H:%M')
d_time1 = datetime.datetime.strptime(str(datetime.datetime.now().date()) + '14:01', '%Y-%m-%d%H:%M')
# current time
n_time = datetime.datetime.now()
#let the program running every 45 second unless time is in time range
while 1>0:
# see if the current time is in time range
    if n_time > d_time and n_time < d_time1:

        #tell the computer where the chrome driver is
        PATH = "D:\Coding_Tools\Python\chromedriver.exe"
        driver = webdriver.Chrome(PATH)

        #open gym booking website
        driver.get("https://hub.ucd.ie/usis/W_HU_MENU.P_PUBLISH?p_tag=GYMBOOK")

        #find the 17:00 row and click on book
        gym_17 = driver.find_element_by_link_text("Book")
        gym_17.click()
        time.sleep(3)

        #go to the 'proceed with booking' page and input username then clcik proceed
        accept_cookie = driver.find_element_by_id("onetrust-accept-btn-handler")
        accept_cookie.click()
        input_username = driver.find_element_by_xpath("//*[@id=\"single-column-content\"]/div/div/div/div[2]/div/form/input[4]")
        input_username.send_keys("21200198")
        proceed = driver.find_element_by_xpath("//*[@id=\"single-column-content\"]/div/div/div/div[2]/div/form/input[5]")
        proceed.click()

        #go to the confirm booking page and click confirm booking
        time.sleep(3)
        confirm = driver.find_element_by_link_text("Confirm Booking")
        confirm.click()
        time.sleep(2)
        print("Booking Successful!")

        driver.quit()
        exit()

    else:
        print('Not the time for booking a slot at 17:00!')
        time.sleep(45)


#-------------------If you want more function, see references below-----------------#
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
