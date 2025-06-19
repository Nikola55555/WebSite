from pages.BasePage import BasePageHelper, BasePageLocators
from pages.modals.login_modal import LoginModalHelper, LoginModalSelectors

import allure
from core.BaseTest import browser

BASE_URL = 'https://urait.ru/'
WRONG_LOGIN_ERROR = 'Неверный формат эл. почты'
WRONG_PASSWORD_ERROR = 'Введите пароль'
TITLE = 'Образовательная платформа Юрайт. Для вузов и ссузов.'


# @allure.suite('Проверка формы авторизации')
# @allure.title('Проверка авторизации при введенном валидном логине и пароле')
# @allure.description(
#     "При отправке формы с заполненным логином 'test' и паролем 'test' система должна показать ошибку 'Неверный формат эл. почты'")
# def test_login_with_valid_login_and_password(browser):
#     BasePageHelper(browser).get_url(BASE_URL)
#     login_modal = LoginModalHelper(browser)
#     login_modal.open_modal_login()
#
#     assert login_modal.is_modal_displayed(), 'Модальное окно не отобразилось'
#
#     login_modal.type_login('bagbee84@mail.ru')
#     login_modal.type_password('47f-]^p{')
#     login_modal.click_submit()
#     print(browser.title)
    # assert error == WRONG_LOGIN_ERROR, 'Ожидался другой текст ошибки'

# @allure.suite('Проверка формы авторизации')
# @allure.title('Проверка появления ошибки при введении невалидного логина и пароля')
# @allure.description(
#         "При отправке формы с заполненным логином 'test' и паролем 'test' система должна показать ошибку 'Неверный формат эл. почты'")
# def test_invalid_login_and_password(browser):
#     BasePageHelper(browser).get_url(BASE_URL)
#     login_modal = LoginModalHelper(browser)
#     login_modal.open_modal_login()
#
#     assert login_modal.is_modal_displayed(), 'Модальное окно не отобразилось'
#
#     login_modal.type_login('test')
#     login_modal.type_password('test')
#     login_modal.click_submit()
#     error = login_modal.get_error_text()
#     assert error == WRONG_LOGIN_ERROR, 'Ожидался другой текст ошибки'

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
    LoginModalHelper.login(browser, 'bagbee84@mail.ru', '47f-]^p{')
    LoginModalHelper.logout(browser)
    assert BasePageHelper.is_on_main_page(browser), f"Ожидали вернуться на https://urait.ru/,  но находимся на {browser.current_url}"