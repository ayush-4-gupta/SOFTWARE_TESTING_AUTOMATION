# https://the-internet.herokuapp.com/


from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser=webdriver.Firefox()
browser.get("https://practice.expandtesting.com/checkboxes")

browser.maximize_window()

browser.execute_script("window.scrollTo(0,document.body.scrollHeight);")
browser.find_element(By.ID,"checkbox1").click()
time.sleep(3)
browser.find_element(By.ID,"checkbox1").click()



# checkboxes=browser.find_elements(By.XPATH,"//input[@type='checkbox']")
# for checkbox in checkboxes:
#     checkbox.send_keys(Keys.space)


# check_box=0
# for i in checkboxes:
#     if i.selected():
#         check_box +=1

# expected_checks=2

# if check_box==expected_checks:
#     print("verified")
# else:
#     print(" not verified")