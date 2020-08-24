from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

EMAIL_ID = "shreya.sharma@sitpune.edu.in"
def slow_typing(element, text):
    for character in text:
        element.send_keys(character)
        time.sleep(0.3)

browser = webdriver.Chrome('./CromeDriver/chromedriver_win32/chromedriver.exe')

browser.get("https://www.amazon.in/")
print(browser.title)

searchbox = browser.find_element_by_id("twotabsearchtextbox")
searchbox.send_keys("kindle books for free")

searchButton = browser.find_element_by_class_name("nav-input")
searchButton.click()
time.sleep(3)
#Select the book
bookNameLink = browser.find_element_by_partial_link_text("Teach")
bookNameLink.click()

#A new tab opens so shift the tab control
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + Keys.TAB)

time.sleep(2)
browser.switch_to.window(browser.window_handles[1])
add_cart = browser.find_element_by_id("add-to-ebooks-cart-button")
add_cart.click()

time.sleep(5)
click_cart = browser.find_element_by_id("a-autoid-0-announce")
click_cart.click()

time.sleep(4)

click_proceed = browser.find_element_by_id("sc-ebooks-buy-box-ptc-button")
click_proceed.click()

print(browser.title)
#Without login, one cannot proceed to checkout
email_phone = browser.find_element_by_id("ap_email")
slow_typing(email_phone,"+917720918651")
continue_email = browser.find_element_by_id("continue")
continue_email.click()
password_user = browser.find_element_by_id("ap_password")
with open('zomatopassword.txt', 'r') as myfile:
    Password = myfile.read().replace('\n', '')
slow_typing(password_user,Password)
login = browser.find_element_by_id("signInSubmit")
login.click()

