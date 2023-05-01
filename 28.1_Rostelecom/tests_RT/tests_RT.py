from settings import *
import pytest
from time import sleep


# EXP-001  Открывается страница с формой "Авторизация"
def test_authorization_is_exists(browser, auth):
    auth.go_to_site()
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_AUTH


# EXP-002, EXP-003
# Базовая позитивная проверка авторизации по валидным телефону/почте и паролю.
# По умолчанию при открытии страницы открыта форма авторизации по телефону -- таб "Телефон"
# При вводе почты таб "Телефон" переключается на таб "Почта"
@pytest.mark.positive
@pytest.mark.parametrize('login', [telephone, email], ids=['telephone', 'email'])
def test_auth_valid_data(browser, auth, login):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, login)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)


# EXP - 004 Авторизация по валидному логину и валидному паролю
@pytest.mark.positive
@pytest.mark.parametrize('login', [login], ids=['login'])
def test_auth_valid_login_pass(browser, auth, login):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, login)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Логин'


# EXP - 005 Авторизация по валидному лицевому счету и валидному паролю
@pytest.mark.positive
@pytest.mark.parametrize('id_count', [id_count], ids=['id_count'])
def test_auth_valid_id_count_pass(browser, auth, id_count):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, id_count)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Лицевой счёт'


# EXP-006,EXP-007
# Авторизация по валидной телефону/почте и невалидному паролю. Появляется сообщение об ошибке.
@pytest.mark.negative
@pytest.mark.parametrize('login', [telephone, email], ids=['telephone', 'email'])
def test_auth_fake_password(browser, auth, login):
    auth.go_to_site()
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, login)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, fake_password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_ERROR_MSG).text == auth.ERROR_MSG_INVALID_DATA


# EXP-008 Авторизация по пустому полю ввода телефона и валидному паролю.  Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_empty_phone(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_PHONE)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_PHONE_MSG


# EXP-009 Авторизация по пустому полю ввода почты и валидному паролю. . Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_empty_mail(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_MAIL_MSG


# EXP-010 Авторизация по пустому полю ввода логина и валидному паролю. Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_empty_login(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(3)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LOGIN_MSG


# EXP-011 Авторизация по пустому полю ввода лицевого счета и валидному паролю.  Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_empty_ls(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LS)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, '')
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_EMPTY_USERNAME_MSG).text == auth.EMPTY_LS_MSG


# EXP-012 Ссылка "Забыл пароль" кликабельна и открывает форму "Восстановление пароля"
def test_forgot_password(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_FORGOT_PASSWORD)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_RECOVERY


# EXP-013 Ссылка "Зарегистрироваться" кликабельна и открывает форму "Регистрация"
def test_register(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_REGISTER)
    assert auth.find_element(auth.LOCATOR_PAGE_RIGHT).text == auth.TITLE_REGISTRATION


# EXP-014 Ссылка "Пользовательское соглашение" кликабельна и открывает форму "Регистрация"
def test_oferta(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_OFERTA)
    browser.switch_to.window(browser.window_handles[1])
    current_url = browser.current_url
    assert current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"


# EXP-015 Авторизация по валидному телефону и паролю при вводе телефона в поле "Логин". Поле"Логин" переключается на
# поле "Телефон".
@pytest.mark.positive
def test_auth_valid_phone_tab_mail(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_MAIL)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, telephone)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, password)
    active_tab_name = auth.find_element(auth.LOCATOR_ACTIVE_TAB).text
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_BTN_LOGOUT)
    assert active_tab_name == 'Телефон'


# EXP-016 Авторизация с XSS в поле ввода логина и невалидному паролю. Появляется сообщение об ошибке.
@pytest.mark.negative
def test_auth_XSS_login(browser, auth):
    auth.go_to_site()
    auth.click_element(auth.LOCATOR_BTN_LOGIN)
    auth.input_data(auth.LOCATOR_INPUT_USERNAME, XSS)
    auth.input_data(auth.LOCATOR_INPUT_PASSWORD, fake_password)
    auth.click_element(auth.LOCATOR_CHECK_BOX)
    sleep(1)
    auth.click_element(auth.LOCATOR_BTN_ENTER)
    assert auth.find_element(auth.LOCATOR_XSS).text == auth.TITLE_XSS

# pytest -v --driver Chrome --driver-path D:\SkillFactory\Skilfactory-qap1013\28.1_Rostelecom\chromedriver_win32\chromedriver.exe tests_RT\tests_RT.py
