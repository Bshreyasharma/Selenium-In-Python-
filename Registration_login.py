from selenium import webdriver
import time

EMAIL_ID = "shreya.sharma@sitpune.edu.in"
def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)

browser = webdriver.Chrome('./CromeDriver/chromedriver_win32/chromedriver.exe')

browser.get("https://www.browserstack.com/")
print(browser.title)

time.sleep(2)

# to accept cookie notification so that it doesn't interfere
cookie_cta = browser.find_element_by_id('accept-cookie-notification')
cookie_cta.click()

create_account = browser.find_element_by_id("signupModalButton")
create_account.click()


username = browser.find_element_by_id('user_full_name')
slow_typing(username,"Shreya Sharma")
time.sleep(2)

email = browser.find_element_by_id('user_email_login')
slow_typing(email, EMAIL_ID)

time.sleep(2)
password = browser.find_element_by_id('user_password')

with open('password.txt', 'r') as myfile:
    Password = myfile.read().replace('\n', '')
slow_typing(password, Password)

time.sleep(1)
toc = browser.find_element_by_name('terms_and_conditions')
toc.click()

signupbutton = browser.find_element_by_id('user_submit')
signupbutton.click()
time.sleep(100)

browser.close()


#--------------------------------Veryfy the login Credentials-----------------------------------------------------------

browser.get("https://www.browserstack.com/")
print(browser.title)
time.sleep(2)

cookie_cta = browser.find_element_by_id('accept-cookie-notification')
cookie_cta.click()
time.sleep(2)

get_started = browser.find_element_by_id("signupModalButton")
get_started.click()
time.sleep(2)

sign_in = browser.find_element_by_class_name("sign-in-link")
sign_in.click()
time.sleep(2)

time.sleep(2)
email_user = browser.find_element_by_id("user_email_login")
slow_typing(email_user, EMAIL_ID)

time.sleep(2)
password_user = browser.find_element_by_id("user_password")
with open('password.txt', 'r') as myfile:
    Password = myfile.read().replace('\n', '')
slow_typing(password_user,Password)

user_submit = browser.find_element_by_id("user_submit")
user_submit.click()

browser.close()