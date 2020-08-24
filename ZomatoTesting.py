from selenium import webdriver
import time

EMAIL_ID = "shreya.sharma@sitpune.edu.in"
def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)

browser = webdriver.Chrome('./CromeDriver/chromedriver_win32/chromedriver.exe')

browser.get("https://www.zomato.com/")
print(browser.title)

time.sleep(4)

create_account = browser.find_element_by_id("signup-link")
create_account.click()

time.sleep(4)
sign_up = browser.find_element_by_id("signup-email")
sign_up.click()
time.sleep(4)

username = browser.find_element_by_id('sd-fullname')
username.send_keys('John Doe')
time.sleep(2)

email = browser.find_element_by_id('sd-email')
slow_typing(email, EMAIL_ID)

time.sleep(1)
toc = browser.find_element_by_id('sd-newsletter')
toc.click()

Registerbutton = browser.find_element_by_id('sd-submit')
Registerbutton.click()
time.sleep(20)

browser.close()
