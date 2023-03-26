import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Open https://SunInJuly.github.io/execute_script.html page .
link = 'https://SunInJuly.github.io/execute_script.html'
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # Read value for variable x.
    x = browser.find_element(By.ID, 'input_value').text


    # Calculate the mathematical function of x
    res = calc(x)

    # Scroll down the page
    browser.execute_script("window.scrollBy(0, 100);")

    # Enter your answer in the text field
    input_1 = browser.find_element(By.ID, 'answer')
    input_1.send_keys(res)

    # Select checkbox "I'm the robot"
    option_1 = browser.find_element(By.ID, 'robotCheckbox')
    option_1.click()

    # Toggle radiobutton "Robots rule!"
    option_2 = browser.find_element(By.ID, 'robotsRule')
    option_2.click()

    # Press the "Submit" button
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary')
    button.click()


finally:

    time.sleep(10)
    # Close browser
    browser.quit()

# Empty line