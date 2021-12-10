import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from  webdriver_manager.chrome import ChromeDriverManager

link = "http://selenium1py.pythonanywhere.com/"

@pytest.fixture(scope="function")
def driver():
    print("\nstart browser for test...")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    yield driver
    print("\nquit browser...")
    driver.quit()


class TestMainPage1():

    def test_guest_should_see_login_link(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, "#login_link")

     def test_guest_should_see_basket_link_on_the_main_page(self, driver):
        driver.get(link)
        driver.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")