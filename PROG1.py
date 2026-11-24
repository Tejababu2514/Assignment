import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://www.facebook.com")
print(driver.title)
time.sleep(10)
driver.quit()

