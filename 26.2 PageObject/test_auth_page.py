from pages.auth_page import AuthPage
import time


def test_auth_page(selenium):
   page = AuthPage(selenium)
   page.enter_email("zzzzz@mail.ru")
   page.enter_pass("zzzzz")
   page.btn_click()

   #знак != или == будет зависеть от того, верные или неверные данные мы вводим
   assert page.get_relative_link() == '/all_pets', "login error"

   time.sleep(5) #задержка для учебных целей


# python -m pytest -v --driver Chrome --driver-path D:\SkillFactory\Skilfactory-qap1013\24Selenium\chromedriver_win32/chromedriver'
#                                     r'.exe test_auth_page.py