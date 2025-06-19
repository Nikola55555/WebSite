import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--lang=ru')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome(options=options)
    yield driver
    if driver:
        driver.quit()