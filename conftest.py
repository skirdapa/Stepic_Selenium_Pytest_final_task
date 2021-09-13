from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    # Браузер пусть будет хром по умолчанию
    parser.addoption('--browser_name', action='store', default='chrome',
                     help='Выберите доступный браузер: chrome или firefox')
    # А вот выбор языка сделаем обязательным параметром: default=None
    parser.addoption("--language", action="store", default="en",
                     help="Выберите язык: ru, en-gb, fr, de и тд.")


# Фикстура браузер, которую будем использовать в остальных тестах
@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    driver = None
    print(f"\nВыбран язык {user_language}")
    if user_language is None:
        raise pytest.UsageError("При запуске не указаны параметры локализации: --language."
                                "Укажите допустимые значения ru, fr, de, su и тд для параметра --language")
    if browser_name == "chrome":
        print("Запускаем Chrome браузер...")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("Запускаем Firefox браузер...")
        fp = webdriver.FirefoxProfile()
        fp.set_preference('intl.accept_languages', user_language)
        driver = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("При запуске не верно указан или отсутствует параметр --browser-name\n"
                                "Используете с допустимыми значениями: chrome или firefox")
    yield driver
    print("...закрываем браузер...")
    driver.quit()
