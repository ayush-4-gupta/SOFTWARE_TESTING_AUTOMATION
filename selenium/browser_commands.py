# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time


# driver=webdriver.Firefox()

# driver.get("https://opensource-demo.orangehrmlive.com/")


# driver.find_element(By.CSS_SELECTOR,".orangehrm-login-forgot-header").click()


# time.sleep(5)

# driver.back()
# time.sleep(2)
# driver.forward()
# time.sleep(2)
# driver.refresh()
# time.sleep(3)
# driver.close()




from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.maximize_window()

driver.get("https://opensource-demo.orangehrmlive.com/")

# Better wait instead of immediate click
driver.implicitly_wait(10)

# Click "Forgot your password?"
driver.find_element(By.CSS_SELECTOR, ".orangehrm-login-forgot-header").click()

time.sleep(3)

# Navigation
driver.back()
time.sleep(2)

driver.forward()
time.sleep(2)

driver.refresh()
time.sleep(2)

# Close browser
driver.quit()