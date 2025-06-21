from pages.base_page import BasePageHelper, BasePageLocators
from pages.modals.login_modal import LoginModalHelper, LoginModalSelectors

import allure
from core.BaseTest import browser

BASE_URL = 'https://urait.ru/'
WRONG_LOGIN_ERROR = 'Неверный формат эл. почты'
WRONG_PASSWORD_ERROR = 'Введите пароль'
TITLE = 'Образовательная платформа Юрайт. Для вузов и ссузов.'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка появления ошибки при введении невалидного логина и пароля')
def test_invalid_login_and_password(browser):
    LoginModalHelper.login(browser, 'test', 'test')
    error = LoginModalHelper(browser).get_error_text()
    assert error == WRONG_LOGIN_ERROR, 'Ожидался другой текст ошибки'


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка авторизации при введенном валидном логине и пароле')
def test_login_with_valid_login_and_password(browser):
    LoginModalHelper.login(browser, 'bagbee84@mail.ru', '47f-]^p{')
    helper = BasePageHelper(browser)
    logined = helper.find_element(LoginModalSelectors.LOGINED).text
    assert "bagbee84@mail.ru" in logined


@allure.suite('Проверка формы авторизации')
@allure.title('Проверка успешного logout')
def test_logout(browser):
    page = BasePageHelper(browser)
    LoginModalHelper.login(browser, 'bagbee84@mail.ru', '47f-]^p{')
    LoginModalHelper.logout(browser)
    assert page.is_on_main_page(), f"Ожидали вернуться на https://urait.ru/,  но находимся на {browser.current_url}"
