import os
from dotenv import load_dotenv
from faker import Faker

dotenv_path = os.path.join(os.path.dirname(__file__),'D:\SkillFactory', '.env')
load_dotenv(dotenv_path)

# Основной URL тестируемого сайта
URL = 'https://b2c.passport.rt.ru'

# Путь к вебдрайверу
PATH = './chromedriver.exe'

# Валидные данные для авторизации
telephone = os.getenv("TELEPHONE")
email = os.getenv("EMAIL")
id_count = os.getenv("ID_COUNT")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")

# Невалидные данные для авторизации
fake = Faker()
fake_password = fake.password()

#XSS инъекция
XSS = '<script>alert(123)</script>'