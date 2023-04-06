import pytest
from selenium.webdriver.common.by import By

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