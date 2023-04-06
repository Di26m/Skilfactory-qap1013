import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_no_copies_pets(show_my_pets):  # 5. В списке нет повторяющихся питомцев. (Сложное задание).

   # Устанавливаем явное ожидание
   WebDriverWait(pytest.driver, 10).until(
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