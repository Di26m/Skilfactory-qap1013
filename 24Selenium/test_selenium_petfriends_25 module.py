import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
import re

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome('D:\SkillFactory\Skilfactory-qap1013\24Selenium\chromedriver_win32/chromedriver'
                                    r'.exe')
   pytest.driver.set_window_size(1900, 1200)
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends.skillfactory.ru/login')

   yield

   pytest.driver.quit()


def test_show_my_pets():
   # Вводим email
   pytest.driver.find_element(By.ID, 'email').send_keys('zzzzz@mail.ru')
   # Вводим пароль
   pytest.driver.find_element(By.ID,'pass').send_keys('zzzzz')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element(By.CSS_SELECTOR,'button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
   assert pytest.driver.find_element(By.TAG_NAME,'h1').text == "PetFriends"

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

def test_sort_my_pets(show_my_pets):

   images = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')
   names = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-title')
   descriptions = pytest.driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-text')

   for i in range(len(names)):
      assert images[i].get_attribute('src') != ''
      assert names[i].text != ''
      assert descriptions[i].text != ''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0

def test_all_pets_in_list(show_my_pets):    # 1. На странице Присутствуют все питомцы.


   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
   all_pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   number = all_pets[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])
   number_of_pets = len(pets)
   assert number == number_of_pets


def test_photo_availability(show_my_pets): # 2.Хотя бы у половины питомцев есть фото.

   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))

   # Сохраняем в переменную ststistic элементы статистики
   statistic = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   # Сохраняем в переменную images элементы с атрибутом img
   images = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover img')

   # Получаем количество питомцев из данных статистики
   number = statistic[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])

   # Находим половину от количества питомцев
   half = number // 2

   # Находим количество питомцев с фотографией
   number_а_photos = 0
   for i in range(len(images)):
      if images[i].get_attribute('src') != '':
         number_а_photos += 1

   # Проверяем что количество питомцев с фотографией больше или равно половине количества питомцев
   assert number_а_photos >= half
   print(f'количество фото: {number_а_photos}')
   print(f'Половина от числа питомцев: {half}')

def test_pets_have_name_age_and_gender(show_my_pets): #3. У всех питомцев есть имя, возраст и порода.


   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах

   data = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')
   # Забираем только первые 3 элемента без   Х
   pet_data = data[:3]
   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу. Находим количество элементов в получившемся списке и сравниваем их
   # с ожидаемым результатом
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '')
      split_data_pet = data_pet.split(' ')
      result = len(split_data_pet)
      assert result == 3

def test_all_pets_have_different_names(show_my_pets): # 4. У всех питомцев разные имена


   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))
   # Сохраняем в переменную pet_data элементы с данными о питомцах
   data = pytest.driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')
   pet_data = data[:3]
   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу.Выбераем имена и добавляем их в список pets_name.
   pets_name = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '')
      split_data_pet = data_pet.split(' ')
      pets_name.append(split_data_pet[0])

   # Перебираем имена и если имя повторяется то прибавляем к счетчику r единицу.
   # Проверяем, если r == 0 то повторяющихся имен нет.
   r = 0
   for i in range(len(pets_name)):
      if pets_name.count(pets_name[i]) > 1:
         r += 1
   assert r == 0
   print(r)
   print(pets_name)


def test_no_copies_pets(show_my_pets):  # 5. В списке нет повторяющихся питомцев. (Сложное задание).

   # Устанавливаем явное ожидание
   element = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   # Сохраняем в переменную pet_data элементы с данными о питомцах
   data = pytest.driver.find_elements(By.CSS_SELECTOR,'.table.table-hover tbody tr')
   pet_data = data[:3]
   # Перебираем данные из pet_data, оставляем имя, возраст, и породу остальное меняем на пустую строку
   # и разделяем по пробелу.
   list_data = []
   for i in range(len(pet_data)):
      data_pet = pet_data[i].text.replace('\n', '')
      split_data_pet = data_pet.split(' ')
      list_data.append(split_data_pet)

   # Склеиваем имя, возраст и породу, получившиеся склееные слова добавляем в строку
   # и между ними вставляем пробел
   line = ''
   for i in list_data:
      line += ''.join(i)
      line += ' '

   # Получаем список из строки line
   list_line = line.split(' ')

   # Превращаем список в множество
   set_list_line = set(list_line)

   # Находим количество элементов списка и множества
   a = len(list_line)
   b = len(set_list_line)

   # Из количества элементов списка вычитаем количество элементов множества
   result = a - b

   # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
   assert result == 0

