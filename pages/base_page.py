import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGO_BUTTON = (By.XPATH, '//div[@class="middle"]/div[@class="logo"]')
    LOGIN_BUTTON = (By.XPATH, '//div[@class="login_register"]/a[text()="Вход"]')
    REGISTRATION_BUTTON = (By.XPATH, '//div[@class="login_register"]/a[text()="Регистрация"]')
    CLOSE_POP_UP = (By.XPATH, '//button[@class="popup-btn-close js-close"]')


class BasePageHelper:
    def __init__(self, driver):
        self.driver = driver

    def check_page(self):
        with allure.step('Проверяем корректность загрузки страницы'):
            self.attach_screenshot()
        self.find_element(BasePageLocators.LOGO_BUTTON)
        self.find_element(BasePageLocators.LOGIN_BUTTON)

    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator),
                                                         message=f"Не удалось найти элемент {locator}")

    def find_elements(self, locator, time=5):
        return WebDriverWait(self.driver, time).until(EC.visibility_of_all_elements_located(locator),
                                                      message=f"Не удалось найти элементы {locator}")

    @allure.step(f'Открываем страницу')
    def get_url(self, url):
        return self.driver.get(url)

    def attach_screenshot(self):
        allure.attach(self.driver.get_screenshot_as_png(), "скриншот", allure.attachment_type.PNG)

    @allure.step(f'Нажимаем кнопку "Войти"')
    def click_login(self):
        self.find_element(BasePageLocators.LOGIN_BUTTON).click()

    @allure.step(f'Нажимаем кнопку "Спасибо, не сейчас" в Pop-up')
    def open_modal_login(self):
        self.find_element(BasePageLocators.CLOSE_POP_UP).click()
        self.click_login()

    @allure.step(f'Получение текущего URL')
    def is_on_main_page(self):
        return self.driver.current_url == "https://urait.ru/"
