import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    button = driver.find_element(By.ID, "submit_button")
    button.click()
finally:
    driver.quit()

