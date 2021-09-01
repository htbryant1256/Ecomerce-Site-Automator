# This program was written to help automate
# posting products to an online store I have
# on redbubble.com.
import time
import os
from selenium import webdriver
# chrome webdriver path, most likely it's this path, if not change to correct path.
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

# log into redbubble
driver.get("https://www.redbubble.com")
# go to login page
driver.find_element_by_link_text("Login").click()

#username password
username = "**************"
password = "**************"

# folder directory for images folder EX: C:/****/****/Desktop/Images/
imageDirectory = "***************"

# logging into account
driver.find_element_by_id("ReduxFormInput1").send_keys(username)
driver.find_element_by_id("ReduxFormInput2").send_keys(password)
# User has to manually solve the Captcha one time, after that the program does the rest.
input("Press Enter To Continue Once Logged In.")

# progam navigates to product posting page
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div/div/header/div[3]/div[1]').click()
driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[2]/div/div/div/header/div[3]/div[1]/div/div/div/div[2]/div/div/div/div/div/ul[1]/div[1]').click()

#input delay to avoid bugs
delay = 0.25

for filename in os.listdir(imageDirectory):
    if filename.endswith(".png") or filename.endswith(".jpg"):
        # image is uploaded
        driver.find_element_by_xpath('//*[@id="select-image-single"]').send_keys(
            imageDirectory + filename)

        # relative tags and settings for the product editing page
        driver.find_element_by_xpath('//*[@id="work_tag_field_en"]').send_keys("photo, art, cool,"
        " military, trippy, zoomer, meme, funny, nature, nerdy,")
        time.sleep(delay)
        driver.find_element_by_xpath('//*[@id="work_tag_field_en"]').click()
        time.sleep(delay)
        # name of product is automatically set to the file name of the photo
        driver.find_element_by_xpath('//*[@id="work_title_en"]').send_keys(filename[:-4])
        time.sleep(delay)
        driver.find_element_by_xpath('//*[@id="media_photography"]').click()
        time.sleep(delay)
        driver.find_element_by_xpath('//*[@id="media_digital"]').click()
        time.sleep(delay)
        driver.find_element_by_xpath('//*[@id="work_safe_for_work_true"]').click()
        time.sleep(delay)
        driver.find_element_by_xpath('//*[@id="rightsDeclaration"]').click()

        # progam sleeps to allow user to make adjustments to the product if needed.
        print("Starting Sleep")
        time.sleep(45)
        print("Ending Sleep")

        # product is posted
        driver.find_element_by_xpath('//*[@id="submit-work"]').click()

        # progam sleeps again to avoid problems with the website being called too often
        print("Starting Sleep")
        time.sleep(120)
        print("Ending Sleep")

        # add another design
        driver.find_element_by_xpath(
            '//*[@id="app"]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div[2]/div/a/span').click()


