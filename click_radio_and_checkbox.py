import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "http://suninjuly.github.io/math.html"
driver = webdriver.Chrome(ChromeDriverManager().install())

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(url)

    input_value = driver.find_element(By.XPATH, "//span[@id='input_value']")
    input_answer = driver.find_element(By.XPATH, "//input[@id='answer']")
    robot_checkbox = driver.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    robot_radiobutton = driver.find_element(By.XPATH, "//input[@id='robotsRule']")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")

    x = input_value.text
    y = calc(x)

    input_answer.send_keys(y)
    robot_checkbox.click()
    robot_radiobutton.click()
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()