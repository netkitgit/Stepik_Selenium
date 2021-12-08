import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
url = "http://suninjuly.github.io/selects1.html"

def calc(a,b):
    return str((a+b))

try:
    driver.get(url)

    num_1 = int(driver.find_element(By.XPATH, "//span[@id='num1']").text)
    num_2 = int(driver.find_element(By.XPATH, "//span[@id='num2']").text)
    answer_dropdown = Select(driver.find_element(By.XPATH, "//select[@id='dropdown']"))
    button = driver.find_element(By.CSS_SELECTOR, "button.btn")

    value = calc(num_1, num_2)
    answer_dropdown.select_by_value(value)
    button.click()

finally:
    time.sleep(10)
    driver.quit()
