import pytest
from selenium import webdriver

from Pages.auth_page import AuthPage
from settings import PATH


@pytest.fixture()
def browser():
    driver = webdriver.Chrome(executable_path=PATH)
    driver.maximize_window()
    yield driver
    driver.quit()

# создаем экземпляр класса, чтобы не создавать его в каждом тесте
@pytest.fixture()
def auth(browser):
    auth = AuthPage(browser)
    return auth