import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_pets_have_name_age_and_gender(show_my_pets): #3. У всех питомцев есть имя, возраст и порода.

   WebDriverWait(pytest.driver, 10).until(
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