from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from settings import URL


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = URL

    # метод открывает сайт
    def go_to_site(self):
        return self.driver.get(self.base_url)

    # метод находит элемент на странице
    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    # метод кликает по элементу на странице
    def click_element(self, locator):
        self.find_element(locator).click()

    # метод вводит данные в строку ввода
    def input_data(self, locator, text):
        self.find_element(locator).send_keys(text)
