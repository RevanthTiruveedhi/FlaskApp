from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import timedelta
import time as t


PATH = "C:\Development\PythonFlask\drivers\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("http://127.0.0.1:5000/")
t.sleep(2)
driver.find_element_by_name("uname").send_keys("Ram")
t.sleep(2)
driver.find_element_by_name("psw").send_keys("ram")
t.sleep(2)
driver.find_element_by_name("login").send_keys(Keys.RETURN)
t.sleep(2)
driver.find_element_by_name("logout").send_keys(Keys.RETURN)
t.sleep(2)
driver.find_element_by_name("create").send_keys(Keys.RETURN)
t.sleep(2)
driver.find_element_by_name("back").send_keys(Keys.RETURN)
t.sleep(2)
driver.find_element_by_name("uname").send_keys("gracy3")
t.sleep(2)
driver.find_element_by_name("psw").send_keys("pwd1")
t.sleep(2)
driver.find_element_by_name("login").send_keys(Keys.RETURN)
t.sleep(2)
driver.find_element_by_name("create").send_keys(Keys.RETURN)
t.sleep(2)
driver.find_element_by_name("usname").send_keys("gracy3")
t.sleep(2)
driver.find_element_by_name("email").send_keys("gracy@gmail.com")
t.sleep(2)
driver.find_element_by_name("psw").send_keys("psw")
t.sleep(2)
driver.find_element_by_name("psw-repeat").send_keys("psw")
t.sleep(2)
driver.find_element_by_name("contact").send_keys("+22556893525")
t.sleep(2)
driver.find_element_by_name("creatsignin").send_keys(Keys.RETURN)
t.sleep(2)
driver.find_element_by_name("logout").send_keys(Keys.RETURN)
t.sleep(2)
driver.quit()