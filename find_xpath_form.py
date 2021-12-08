import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_xpath_form"
driver = webdriver.Chrome(ChromeDriverManager().install())

try:
    driver.get(link)

    input1 = driver.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = driver.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")
    input3 = driver.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")
    input4 = driver.find_element(By.ID, "country")
    input4.send_keys("Russia")
    button = driver.find_element(By.XPATH, "//button[@type='submit']")
    button.click()
finally:
    time.sleep(30)
    driver.quit()

    # не забываем пустую строку в конце файл иначе в юниксе не выполняется последняя строка

