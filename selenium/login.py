from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Firefox()

# driver.get("https://www.saucedemo.com/")
 
username="standard_user"
password="secret_sauce"
login_url="https://www.saucedemo.com/"


driver.get(login_url)
username_feild=driver.find_element(By.ID,"user-name")

password_feild=driver.find_element(By.ID,"password")

username_feild.send_keys(username)

password_feild.send_keys(password)


login_btn=driver.find_element(By.ID,"login-button")
assert not login_btn.get_attribute("disabled")

login_btn.click()


sucess_element=driver.find_element(By.CSS_SELECTOR,".title")

assert sucess_element.text=="Products"