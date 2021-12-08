import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

url = "http://suninjuly.github.io/redirect_accept.html"
driver = webdriver.Chrome(ChromeDriverManager().install())

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(url)

    want_to_go_button = driver.find_element(By.XPATH, "//button[contains(@class,'btn')]")
    want_to_go_button.click()

    time.sleep(2)

    first_window = driver.window_handles[0]
    new_window = driver.window_handles[1]

    driver.switch_to.window(new_window)

    x_value = driver.find_element(By.XPATH, "//span[@id='input_value']")
    input_answer = driver.find_element(By.XPATH, "//input[@id='answer']")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")

    x = int(x_value.text)
    y = calc(x)

    input_answer.send_keys(y)
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
