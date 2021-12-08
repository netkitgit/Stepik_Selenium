import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestSelectorsUniqal(unittest.TestCase):
    def test_registration_page_1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        url = "http://suninjuly.github.io/registration1.html"
        driver.get(url)

        input_first_name = driver.find_element(
            By.XPATH,
            "//label[contains(text(), 'First name')]/following-sibling::input")

        input_last_name = driver.find_element(
            By.XPATH,
            "//label[contains(text(), 'Last name')]/following-sibling::input")

        input_email = driver.find_element(
            By.XPATH,
            "//label[contains(text(), 'Email')]/following-sibling::input")

        button = driver.find_element(
            By.CSS_SELECTOR,
            "button.btn")

        input_first_name.send_keys("firstName")
        input_last_name.send_keys("lastName")
        input_email.send_keys("email")
        button.click()

        time.sleep(1)

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!",
            "Текст об успешной регистрации не найден")

        driver.quit()

    def test_registration_page_2(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())

        url = "http://suninjuly.github.io/registration2.html"
        driver.get(url)

        input_first_name = driver.find_element(
            By.XPATH,
            "//label[contains(text(), 'First name')]/following-sibling::input")

        input_last_name = driver.find_element(
            By.XPATH,
            "//label[contains(text(), 'Last name')]/following-sibling::input")

        input_email = driver.find_element(
            By.XPATH,
            "//label[contains(text(), 'Email')]/following-sibling::input")

        button = driver.find_element(
            By.CSS_SELECTOR,
            "button.btn")

        input_first_name.send_keys("firstName")
        input_last_name.send_keys("lastName")
        input_email.send_keys("email")
        button.click()

        time.sleep(1)

        welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text

        self.assertEqual(
            welcome_text,
            "Congratulations! You have successfully registered!",
            "Текст об успешной регистрации не найден")

        driver.quit()

if __name__ == '__main__':
    unittest.main()
