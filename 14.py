import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
time.sleep(3)
# This command will scroll the page 100 pixels down
browser.execute_script("window.scrollBy(0, 100);")
time.sleep(3)
button = browser.find_element(By.TAG_NAME, "button")
button.click()

