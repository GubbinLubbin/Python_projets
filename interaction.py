from selenium import webdriver
from selenium.webdriver.common.by import By
driver_options = webdriver.ChromeOptions()
driver_options.add_experimental_option("detach", True)
webdriver=webdriver.Chrome(options=driver_options)
webdriver.get("https://en.wikipedia.org/wiki/Main_Page")
active_editors=webdriver.find_element(By.CSS_SELECTOR,"#articlecount a")
print(active_editors.text)
webdriver.close()