from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class AuthPage(BasePage):
    # локаторы
    LOCATOR_PAGE_RIGHT = (By.XPATH, '//*[@id="page-right"]/div/div/h1')
    LOCATOR_BTN_PHONE = (By.XPATH, "//*[@id='t-btn-tab-phone']")
    LOCATOR_BTN_MAIL = (By.XPATH, "//*[@id='t-btn-tab-mail']")
    LOCATOR_BTN_LOGIN = (By.XPATH, "//*[@id='t-btn-tab-login']")
    LOCATOR_BTN_LS = (By.XPATH, "//*[@id='t-btn-tab-ls']")
    LOCATOR_INPUT_MAIL = (By.XPATH, '//*[@id="page-right"]/div/div/div/form/div[1]/div[2]/div/span[2]')
    LOCATOR_INPUT_USERNAME = (By.ID, 'username')
    LOCATOR_INPUT_PASSWORD = (By.ID, 'password')
    LOCATOR_BTN_ENTER = (By.ID, 'kc-login')
    LOCATOR_BTN_LOGOUT = (By.ID, 'logout-btn')
    LOCATOR_ERROR_MSG = (By.XPATH, "//span[@id='form-error-message']")
    LOCATOR_EMPTY_USERNAME_MSG = (By.CSS_SELECTOR, '.rt-input-container__meta--error')
    LOCATOR_FORGOT_PASSWORD = (By.ID, 'forgot_password')
    LOCATOR_REGISTER = (By.XPATH, "//a[@id='kc-register']")
    LOCATOR_ACTIVE_TAB = (By.CSS_SELECTOR, '.rt-tab.rt-tab--small.rt-tab--active')
    LOCATOR_CHECK_BOX = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[3]/div[1]/span[1]')
    LOCATOR_OFERTA = (By.XPATH, '//*[@id="page-right"]/div[1]/div[1]/div[1]/form[1]/div[4]/a[1]')
    # LOCATOR_XSS = (By.XPATH, '/html/body/h2/text()[1]')
    LOCATOR_XSS = (By.XPATH, "//*[contains(text(), 'Ваш запрос был отклонен из соображений безопасности.')]")
    # тексты сообщений
    ERROR_MSG_INVALID_DATA = 'Неверный логин или пароль'
    ERROR_MSG_INVALID_CAPTCHA = 'Неверно введен текст с картинки'
    EMPTY_PHONE_MSG = 'Введите номер телефона'
    EMPTY_MAIL_MSG = 'Введите адрес, указанный при регистрации'
    EMPTY_LOGIN_MSG = 'Введите логин, указанный при регистрации'
    EMPTY_LS_MSG = 'Введите номер вашего лицевого счета'
    TITLE_AUTH = 'Авторизация'
    TITLE_RECOVERY = 'Восстановление пароля'
    TITLE_REGISTRATION = 'Регистрация'
    TITLE_XSS = 'Ваш запрос был отклонен из соображений безопасности.\nОбратитесь в техническую поддержку по номеру ' \
                '8 (800) 1000 800.'