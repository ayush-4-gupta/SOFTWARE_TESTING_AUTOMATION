from selenium import webdriver
from selenium.webdriver.common.by import By

# driver=webdriver.Chrome()
driver=webdriver.Firefox()
# driver.get("https://www.facbook.com")
driver.get("https://selenium.dev/")

# driver.maximize_window()

title=driver.title
print(title)
assert "Selenium" in title


# -------------------------------------------------------
#   id,name,classname,tagname, linktext,partial linktext,xpath,css selector 




driver.findElement(By.xpath("/html/body/div/main/section[1]/div/div/div/h1"))
