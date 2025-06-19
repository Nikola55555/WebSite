from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePageHelper
import allure

BASE_URL = 'https://urait.ru/'


class LoginModalSelectors:
    MODAL_SELECTOR = (By.XPATH, '//*[@id="login-form"]')
    EMAIL_INPUT = (By.XPATH, '//input[@placeholder="Введите эл. почту"]')
    PASSWORD_INPUT = (By.XPATH, '//input[@id="password"]')
    SUBMIT_BUTTON = (By.XPATH, '//button[contains(text(), "Войти")]')
    ERROR_TEXT = (By.XPATH, '(//div[@class="validationMessage"])[1]')
    LOGINED = (By.XPATH, '//div[@class="user_email"]')
    USER_MENU = (By.XPATH, '//div[@class="top_avatar"]')
    LOGOUT_BUTTON = (By.XPATH, '//div[@class="header-user-exit"]')



class LoginModalHelper(BasePageHelper):
    def __init__(self, driver):
        self.driver = driver
        self.check_page()

    def is_modal_displayed(self):
        modal = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(LoginModalSelectors.MODAL_SELECTOR)
        )
        return modal

    @allure.step('Заполняем поле логин')
    def type_login(self, login):
        self.driver.find_element(*LoginModalSelectors.EMAIL_INPUT).send_keys(login)
        self.attach_screenshot()

    @allure.step('Заполняем поле пароль')
    def type_password(self, password):
        self.attach_screenshot()
        self.driver.find_element(*LoginModalSelectors.PASSWORD_INPUT).send_keys(password)

    @allure.step('Нажимаем на кнопку "Войти"')
    def click_submit(self):
        self.attach_screenshot()
        self.driver.find_element(*LoginModalSelectors.SUBMIT_BUTTON).click()

    @allure.step('Получаем текст ошибки')
    def get_error_text(self):
        self.attach_screenshot()
        return self.find_element(LoginModalSelectors.ERROR_TEXT).text

    @allure.step('Проводим авторизацию пользователя')
    def login(self, email, password):
        BasePageHelper(self).get_url(BASE_URL)
        login_modal = LoginModalHelper(self)
        login_modal.open_modal_login()

        assert login_modal.is_modal_displayed(), 'Модальное окно не отобразилось'

        login_modal.type_login(email)
        login_modal.type_password(password)
        login_modal.click_submit()

    @allure.step('Logout пользователя')
    def logout(self):
        self.find_element(*LoginModalSelectors.USER_MENU).click()
        self.find_element(*LoginModalSelectors.LOGOUT_BUTTON).click()