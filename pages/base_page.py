from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

# класс базовой страницы

class BasePage():
    #driver - текущий драйвер браузера
    #Url - передаваемый url
    #timeout=10 - таймаут ожидания элемента, по умолчанию 10
    def __init__(self, driver, url, timeout=10):
        self.driver = driver
        self.url = url
        self.driver.implicitly_wait(timeout)
        # Всегда разворачиваем максимально окно
        self.driver.maximize_window()

    # Открыть ссылку
    def open(self):
        self.driver.get(self.url)

    # Функция выставляет параметры для проверки существования объекта
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True

    # Функция выставляет параметры для проверки НЕсуществования объекта
    def is_not_element_present(self, how, what, timeout=3):
        try:
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False
