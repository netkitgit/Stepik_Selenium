import os.path
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file_upload.txt')

try:
    driver.get(url)

    input_fist_name = driver.find_element(By.XPATH, "//label[contains(text(), 'First name')]/following-sibling::input[1]")
    input_last_name = driver.find_element(By.XPATH, "//label[contains(text(), 'Last name')]/following-sibling::input[1]")
    input_email = driver.find_element(By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input[1]")
    input_file = driver.find_element(By.XPATH, "//input[@id='file']")
    submit_button = driver.find_element(By.CSS_SELECTOR, "button.btn")

    input_fist_name.send_keys('Name')
    input_last_name.send_keys('Last')
    input_email.send_keys('email@email.cpm')
    input_file.send_keys(file_path)

    submit_button.click()

finally:
    time.sleep(10)
    driver.quit()
