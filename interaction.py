from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=driver_options)
driver.get("http://secure-retreat-92358.herokuapp.com")
first_name=driver.find_element(By.NAME,value="fname")
first_name.send_keys("Ankit")
last_name=driver.find_element(By.NAME,value="lname")
last_name.send_keys("Silwal")
gmail=driver.find_element(By.NAME,value="email")
gmail.send_keys("studypurposes911@gmail.com")
btn=driver.find_element(By.CSS_SELECTOR,"formbtn")
btn.click()