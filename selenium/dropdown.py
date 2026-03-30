from selenium import webdriver
from selenium.webdriver.common.by import By
import time



from selenium.webdriver.support.select import Select


driver=webdriver.Firefox()

# driver.maximize_window()
login_url="https://the-internet.herokuapp.com/dropdown"

driver.get(login_url)

dropdown_element=driver.find_element(By.ID,"dropdown")
select=Select(dropdown_element)


# 3 ways
## select the value by visible text 
# #select the value by index
# #select the option by using a value

select.select_by_visible_text("Option 2")
# select.select_by_visible_text("Option 1")


select.select_by_index(1)
# index-->0,1,2

select.select_by_value("2")


time.sleep(2)
driver.close()




# to count no. of options
 
# option_count=len(select.options)

# expected=4
# if option_count==expected:
#     print("verified")
# else:
#     print(" not verified")
