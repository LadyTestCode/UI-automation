import pytest
from selenium import webdriver

# Описываем дополнительные опции командной строки
# --bro - браузер, на котором будет выполняться тестирование
def pytest_addoption(parser):
    parser.addoption ("--bro",
                      action="store",
                      default="Chrome",
                      help='available browsers: IE, Chrome, Edge, Firefox',
                      choices=("IE", "Chrome","Edge", "FF")
                      )

# Фикстура браузера
@pytest.fixture (autouse=True, scope="session")
def bro(pytestconfig):
    bro = pytestconfig.getoption("bro")
    yield bro

# Фикстура драйвера для запуска браузера
@pytest.fixture(scope="session")
def browser(bro):
    try:
        if bro == "Chrome":
            driver = webdriver.Chrome("/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos")
        elif bro == "IE":
            driver = webdriver.Ie("/Users/20071554/Downloads/IE")
        elif bro == "FF":
            driver = webdriver.Firefox("/Users/20071554/Downloads/FF")
        else:
            driver = webdriver.Edge("/Users/20071554/Downloads/Edge")
        yield driver
    finally:
        #Закрываем браузер
        driver.quit()