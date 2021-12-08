import math
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

url = "http://suninjuly.github.io/wait1.html"

driver = webdriver.Chrome(ChromeDriverManager().install())
#driver.implicitly_wait(5)

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    driver.get(url)

    #verify_button = driver.find_element(By.ID, "verify")

    verify_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
    )

    verify_button.click()

    message = driver.find_element(By.ID, "verify_message")

    assert "successful" in message.text

finally:
    time.sleep(10)
    driver.quit()
