import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

url ="http://suninjuly.github.io/explicit_wait2.html"

driver = webdriver.Chrome(ChromeDriverManager().install())
wait = WebDriverWait(driver, 15)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(url)
    good_price = wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))

    button_book = driver.find_element(By.ID, "book")
    button_book.click()

    math_text = wait.until(EC.text_to_be_present_in_element((By.ID, "simple_text"), "Math is real magic"))
    x_value = driver.find_element(By.ID, "input_value").text
    y_value = calc(int(x_value))

    input_answer = driver.find_element(By.ID, "answer")
    input_answer.send_keys(y_value)

    submit_button = driver.find_element(By.ID, "solve")
    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
