import pytest

from selenium.webdriver.common.by import By


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('zzzzz@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('zzzzz')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME,'h1').text == "PetFriends"