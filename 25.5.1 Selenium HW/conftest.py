import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver


@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('D:\SkillFactory\Skilfactory-qap1013\24Selenium\chromedriver_win32/chromedriver'
                                    r'.exe')
   pytest.driver.set_window_size(1900, 1200)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


@pytest.fixture
def show_my_pets():

   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('zzzzz@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('zzzzz')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()
   # pytest.driver.find_element(By.XPATH, "//a[contains(@href, '/my_pets')]").click()