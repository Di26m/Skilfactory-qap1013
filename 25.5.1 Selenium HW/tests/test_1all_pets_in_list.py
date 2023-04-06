import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def test_all_pets_in_list(show_my_pets):    # 1. На странице Присутствуют все питомцы.


   WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".\\.col-sm-4.left")))
   all_pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")

   WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, ".table.table-hover tbody tr")))

   pets = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

   number = all_pets[0].text.split('\n')
   number = number[1].split(' ')
   number = int(number[1])
   number_of_pets = len(pets)
   assert number == number_of_pets