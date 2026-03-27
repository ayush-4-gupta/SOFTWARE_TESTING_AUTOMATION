
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

viewports=[(1024,768),(768,1024),(375,667),(414,896)]


driver = webdriver.Chrome()
driver.get("https://www.google.com")

try:
    for width,height in viewports:

        driver.set_window_size(768,1024)
        time.sleep(3)
finally:
    driver.close()


driver.close()