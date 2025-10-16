import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session')
def setup_firefox():
    firefox_options = webdriver.FirefoxOptions()

    firefox_options.add_argument('--width=1920')
    firefox_options.add_argument('--height=1080')

    # Создаем драйвер для Firefox
    driver = webdriver.Firefox(options=firefox_options)
    browser.config.driver = driver


# Использование
