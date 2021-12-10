import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test...")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    print("\nquite browser...")
    driver.quit()

@pytest.mark.parametrize('language', ["ru", "en-gd"])
def test_should_see_login_link(driver, language):
    link = f"http://selenium1py.pythonanywhere.com/{language}/"
    driver.get(link)
    driver.find_element(By.CSS_SELECTOR, "#login_link")
