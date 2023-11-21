import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#для возможности ожидать загружающийся элемент:
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#для использования кнопок:
from selenium.webdriver.common.keys import Keys
import locators as locators
from Steps import steps as support_steps

def test_elements_sber_main_page():
    try:
       # driver = webdriver.Chrome('/usr/local/bin/chromedriver/chromedriver')
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        # Открываем главную страницу
        driver.get("http://www.sberbank.ru/")
        # Раскрываем окно на полный экран
        driver.maximize_window()
        # Ожидаем 5 секунд для прорисовки
        time.sleep(5)
        driver.find_element_by_tag_name("span")
        #driver.find_element_by_id("main-page")
        #driver.find_element_by_css_selector("#main-page > div")
        driver.find_element_by_xpath(locators.SBERONLINE_LINK)
        driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/following::div[1]")
        driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/following::div[1]/a[1]")
        driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/parent::div[1]")
        driver.find_element_by_xpath(locators.EXCHANGE_RATES_LINK)

        #Домашнее задание - поиск элементов:
        driver.find_element_by_xpath(locators.GEOPOSITION_LINK)
        driver.find_element_by_xpath("//a[text()=\"ENG\"]")
        driver.find_element_by_xpath(locators.OPEN_SEARCH_LINK)

        #Выполнение действий с найденными элементами - и возврат на предыдущую вкладку:
        sberonline_button = driver.find_element_by_xpath(locators.SBERONLINE_LINK)
        sberonline_button.click()
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)

        #button_individ = driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
        #Имитируем наведение мыши для получения всплывающей подсказки
        #ActionChains(driver).move_to_element(button_individ).perform()
        #time.sleep(5)

        geo_button = driver.find_element_by_xpath(locators.GEOPOSITION_LINK)
        print("geo_button =", geo_button.text)
        geo_button.click()
        region_name_field = driver.find_element_by_xpath("//input[@aria-label=\"Введите имя региона\"]")
        region_name_field.send_keys("Какая-то область")
        time.sleep(2)
        region_name_field.clear()
        time.sleep(2)
        region_name_field.send_keys("Ростовская область")
        region_name_button = driver.find_element_by_xpath(locators.ROSTOV_REGION_FIELD)
        region_name_button.click()
        time.sleep(5)

        #Ожидаем доступности элемента и только потом нажимаем на него:
        button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, locators.GEOPOSITION_LINK)))
        button.click()

        #Прокрутим страницу вниз:
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(5)
    finally:
        driver.quit()

#тест - проверка наведения курсора мыши на объект
def test_mouse_over_menu():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        # Открываем главную страницу
        driver.get("http://www.sberbank.ru/")
        # Раскрываем окно на полный экран
        driver.maximize_window()
        # Ожидаем 5 секунд для прорисовки
        time.sleep(5)
        # Имитируем наведение мыши на элементы - 3 задание домашней работы:
        button_cources = driver.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]")
        ActionChains(driver).move_to_element(button_cources).perform()
        time.sleep(5)

        button_offices = driver.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]/following::a[1]")
        ActionChains(driver).move_to_element(button_offices).perform()
        time.sleep(5)

        button_atm = driver.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]/following::a[2]")
        ActionChains(driver).move_to_element(button_atm).perform()
        time.sleep(5)

        button_geo = driver.find_element_by_xpath(locators.GEOPOSITION_LINK)
        ActionChains(driver).move_to_element(button_geo).perform()
        time.sleep(5)

        button_language = driver.find_element_by_xpath("//a[text()=\"ENG\"]")
        ActionChains(driver).move_to_element(button_language).perform()
        time.sleep(5)

        button_search = driver.find_element_by_xpath(locators.OPEN_SEARCH_LINK)
        ActionChains(driver).move_to_element(button_search).perform()
        time.sleep(5)
    finally: driver.quit()


# тест проверяет переключения на английский язык
def test_change_language_sber_main_page():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        # Открываем главную страницу
        driver.get("http://www.sberbank.ru/")
        # Раскрываем окно на полный экран
        driver.maximize_window()
        # Ожидаем 5 секунд для прорисовки
        time.sleep(5)
        language_button = driver.find_element_by_xpath("//a[text()=\"ENG\"]")
        language_button.click()
        time.sleep(5)
    finally:
        driver.quit()

# тест проверяет поиск по слову Кредит и отсутствие вариантов поиска по сочетанию Кабриолет салатовый
def test_check_search_sber_main_page():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        # Открываем главную страницу
        driver.get("http://www.sberbank.ru/")
        # Раскрываем окно на полный экран
        driver.maximize_window()
        # Ожидаем 5 секунд для прорисовки
        time.sleep(5)
        search_element= driver.find_element_by_xpath(locators.OPEN_SEARCH_LINK)
        search_element.click();
        time.sleep(5)
        #открываем поисковую строку
        search_field = driver.find_element_by_xpath(locators.SEARCH_FIELD_LINK)
        search_field.send_keys("Кредит")
        time.sleep(5)
        #Нажимаем Найти и видим результаты поиска
        search_button = driver.find_element_by_xpath("//button[text()='Найти']")
        search_button.click()
        time.sleep(5)

        search_element = driver.find_element_by_xpath(locators.OPEN_SEARCH_LINK)
        search_element.click();
        search_field = driver.find_element_by_xpath(locators.SEARCH_FIELD_LINK)
        search_field.send_keys("Кабриолет салатовый")
        time.sleep(5)
    #Пробуем найти это слово в выпадающем списке и видим, вариантов нужных нет
        search_name_button = driver.find_elements_by_xpath("//button[text() = \"Кабриолет салатовый\"]")
        assert len(search_name_button) == 0
        time.sleep(5)
        #Ищем элемент Закрыть поиск:
        close_search_button = driver.find_element_by_xpath("//button[text()='Закрыть поиск']")
        close_search_button.click()
        #Реализуем подсчет элементов, удовлетворяющих условию поиска:
        exchange_rates_count = driver.find_elements_by_xpath(locators.EXCHANGE_RATES_LINK)
        print("count курсы валют =", len(exchange_rates_count))

        #Посчитаем количество элементов Офисы и Банкоматы
        offices_rates_count = driver.find_elements_by_xpath(locators.OFFICES_LINK)
        print("count офисы =", len(offices_rates_count))
        bankomates_rates_count = driver.find_elements_by_xpath(loators.ATM_LINK)
        print("count банкоматы =", len(bankomates_rates_count))
    finally:
        driver.quit()

#Домашнее задание: тест  на проверку скроллинга и переключения между вкладками.
def test_change_tab_and_scroll():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        # Открываем главную страницу
        driver.get("http://www.sberbank.ru/")
        # Раскрываем окно на полный экран
        driver.maximize_window()
        # Ожидаем 5 секунд для прорисовки
        time.sleep(5)
        sberonline_button = driver.find_element_by_xpath(locators.SBERONLINE_LINK)
        sberonline_button.click()
        time.sleep(5)
        #из новой открытой вкладки возвращаемся в исходную
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        #затем снова в новую вкладку и снова возвращеаемся назад:
        driver.switch_to.window(driver.window_handles[1])
        time.sleep(5)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        #скролл вниз на один экран
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(5)
        #скролл вниз до футера
        driver.find_element_by_tag_name('body').send_keys(Keys.END)
        time.sleep(5)
        #скролл вверх на один экран
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
        time.sleep(5)
        #скрол вверх до хедера
        driver.find_element_by_tag_name('body').send_keys(Keys.HOME)
        time.sleep(5)
    finally:
        driver.quit()

# тест проверки выбора геолокации
def test_check_geopostion():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        geo_button = driver.find_element_by_xpath(locators.GEOPOSITION_LINK)
        geo_button.click()
        region_name_field = driver.find_element_by_xpath("//input[@aria-label=\"Введите имя региона\"]")
        region_name_field.send_keys("Ростовская область")
        region_name_button = driver.find_element_by_xpath(locators.ROSTOV_REGION_FIELD)
        region_name_button.click()
        geo_button = driver.find_element_by_xpath(locators.GEOPOSITION_LINK)
        assert geo_button.text == "Ростовская область"
    finally:
        driver.quit()

def test_incorrect_geoposition():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        geo_button = driver.find_element_by_xpath(locators.GEOPOSITION_LINK)
        geo_button.click()
        time.sleep(3)
        region_name_field = driver.find_element_by_xpath(locators.REGION_NAME_FIELD)
        region_name_field.send_keys(support_steps.generate_random_string(5))
        time.sleep(5)
    finally:
        driver.quit()

#---------------------------------- Home work -------------------

#тест для проверки перехода по ссылкам - открытие правильной страницы - курсы валют
def test_moving_menu_links_exchange():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        exchange_rates_button = driver.find_element_by_xpath(locators.EXCHANGE_RATES_LINK)
        exchange_rates_button.click()
        time.sleep(5)
        first_page_title = driver.find_element_by_xpath(locators.FIRST_TITLE_ON_PAGE)
        print(first_page_title.text)
        assert first_page_title.text == "Курсы валют"
    finally:
        driver.quit()

#тест для проверки перехода по ссылкам - открытие правильной страницы - офисы
def test_moving_menu_links_offices():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        offices_rates_button = driver.find_element_by_xpath(locators.OFFICES_LINK)
        offices_rates_button.click()
        time.sleep(5)
        first_page_title = driver.find_element_by_xpath(locators.FIRST_TITLE_ON_PAGE)
        assert first_page_title.text == "Офисы и банкоматы"
    finally:
        driver.quit()

#тест для проверки перехода по ссылкам - открытие правильной страницы - сбербанк онлайн
def test_moving_menu_links_sbol():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        sbol_rates_button = driver.find_element_by_xpath(locators.SBERONLINE_LINK)
        sbol_rates_button.click()
        time.sleep(5)
        first_page_title = driver.find_element_by_xpath(locators.FIRST_TITLE_ON_PAGE)
        assert first_page_title.text == "СберБанк"
    finally:
        driver.quit()

#тест для проверки перехода по ссылкам - открытие правильной страницы -банкоматы
def test_moving_menu_links_boxes():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        boxes_rates_button = driver.find_element_by_xpath(locators.ATM_LINK)
        boxes_rates_button.click()
        time.sleep(5)
        first_page_title = driver.find_element_by_xpath(locators.FIRST_TITLE_ON_PAGE)
        assert first_page_title.text == "Офисы и банкоматы"
    finally:
        driver.quit()

#параметризованный тест для проверки перехода с главной страницы по пунктам меню
@pytest.mark.parametrize('element_menu, element_title, element_text',
                         [
                          (locators.EXCHANGE_RATES_LINK, locators.FIRST_TITLE_ON_PAGE, "Курсы валют"),
                          (locators.OFFICES_LINK, locators.FIRST_TITLE_ON_PAGE, "Офисы и банкоматы"),
                          (locators.SBERONLINE_LINK, locators.FIRST_TITLE_ON_PAGE, "СберБанк"),
                          (locators.ATM_LINK, locators.FIRST_TITLE_ON_PAGE, "Офисы и банкоматы"),
                         ],
                         ids=["Exchange", "Offices", "Sbol", "ATM"]
                         )
def test_moving_menu_links_parametrized(element_menu, element_title, element_text):
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        time.sleep(5)
        menu_button = driver.find_element_by_xpath(element_menu)
        menu_button.click()
        time.sleep(5)
        first_page_title = driver.find_element_by_xpath(element_title)
        assert first_page_title.text == element_text
    finally:
        driver.quit()

#тест подсчета элементов на странице
def test_count_links():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        exchange_rates_count = driver.find_elements_by_xpath(locators.EXCHANGE_RATES_LINK)
        print("count курсы валют =", len(exchange_rates_count))
        assert len(exchange_rates_count) == 4
        #далее проверим для остальных элементов: "Офисы", "Банкоматы", "СберБанк Онлайн".

        sberonline_rates_count = driver.find_elements_by_xpath(locators.SBERONLINE_LINK)
        print("count сбер онлайн =", len(sberonline_rates_count))
        assert len(sberonline_rates_count) == 1

        offices_rates_count = driver.find_elements_by_xpath(locators.OFFICES_LINK)
        print("count офисы =", len(offices_rates_count))
        assert len(offices_rates_count) == 3

        boxes_rates_count = driver.find_element_by_xpath(locators.ATM_LINK)
        print("count банкоматы =", len(boxes_rates_count))
        assert len(boxes_rates_count) == 3
    finally:
        driver.quit()

#тест для проверки изменения цвета ссылок при наведении мыши
def test_color_link():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        sberonline_button = driver.find_element_by_xpath(locators.SBERONLINE_LINK)
        color_before_perform = sberonline_button.value_of_css_property("color")
        ActionChains(driver).move_to_element(sberonline_button).perform()
        color_after_perform = sberonline_button.value_of_css_property("color")
        assert color_before_perform != color_after_perform

    #проверим остальные ссылки: "Курсы валют", "Офисы", "Банкоматы".
        exchange_button = driver.find_element_by_xpath(locators.EXCHANGE_RATES_LINK)
        color_before_perform = exchange_button.value_of_css_property("color")
        ActionChains(driver).move_to_element(exchange_button).perform()
        color_after_perform = exchange_button.value_of_css_property("color")
        assert color_before_perform != color_after_perform

        offices_button = driver.find_element_by_xpath(locators.OFFICES_LINK)
        color_before_perform = offices_button.value_of_css_property("color")
        ActionChains(driver).move_to_element(offices_button).perform()
        color_after_perform = offices_button.value_of_css_property("color")
        assert color_before_perform != color_after_perform

        boxes_button = driver.find_element_by_xpath(locators.ATM_LINK)
        color_before_perform = boxes_button.value_of_css_property("color")
        ActionChains(driver).move_to_element(boxes_button).perform()
        color_after_perform = boxes_button.value_of_css_property("color")
        assert color_before_perform != color_after_perform
    finally:
        driver.quit()

#Тест с проверками корректности заголовков страниц для сценария перехода между страницами
def test_correctness_of_headers_for_pages():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        driver.get("http://www.sberbank.ru/")
        driver.maximize_window()
        first_page_title = driver.find_element_by_xpath("//h2")
        print(first_page_title.text)
        assert first_page_title.text == "Лучшие предложения"
        #находим ссылку и переходим на страницу Сбербанк Онлайн
        sberonline_button = driver.find_element_by_xpath(locators.SBERONLINE_LINK)
        sberonline_button.click()
        new_page_title = driver.find_element_by_xpath(locators.FIRST_TITLE_ON_PAGE)
        time.sleep(5)
        print(new_page_title.text)
        assert new_page_title.text == "СберБанк"
        # из новой открытой вкладки возвращаемся в исходную
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(5)
        #проверяем, что это главная страница
        first_page_title = driver.find_element_by_xpath("//h2")
        print(first_page_title.text)
        assert first_page_title.text == "Лучшие предложения"
    finally:
        driver.quit()

# тест проверяет корректность работы поиска
def test_check_search_sber_main_page():
    try:
        driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
        driver.implicitly_wait(10)
        # Открываем главную страницу
        driver.get("http://www.sberbank.ru/")
        # Раскрываем окно на полный экран
        driver.maximize_window()
        # Ожидаем 5 секунд для прорисовки
        time.sleep(5)
        search_element = driver.find_element_by_xpath(locators.OPEN_SEARCH_LINK)
        search_element.click();
        time.sleep(5)
        #открываем поисковую строку и вводим слово Вклад для поиска
        search_field = driver.find_element_by_xpath(locators.SEARCH_FIELD_LINK)
        search_field.send_keys("Вклад")
        time.sleep(5)
        #Нажимаем Найти
        search_button = driver.find_element_by_xpath("//button[text()='Найти']")
        search_button.click()
        time.sleep(5)
        #Убеждаемся, что мы перешли на страницу поиска
        search_page_fields = driver.find_elements_by_xpath("//input[@type=\"search\" and @placeholder = \"Что-нибудь поищем\"]")
        assert len(search_page_fields) >=1
        #Проверим, что какие то результаты по нашему поиску есть
        search_results = driver.find_elements_by_xpath("//yass-span")
        assert len(search_results) >= 1
        #Пробуем найти чертополох и убждаемся, что корректно обрабатываются пустые результаты поиска
        search_page_field = driver.find_element_by_xpath("//input[@type=\"search\" and @placeholder = \"Что-нибудь поищем\"]")
        search_page_field.clear()
        search_page_field.send_keys("Чертополох")
        search_button = driver.find_element_by_xpath("//input[@type=\"button\"]")
        search_button.click()
        time.sleep(3)
        incorrect_search_results = driver.find_element_by_xpath("(//yass-div)[4]")
        print(incorrect_search_results.text)
        assert incorrect_search_results.text == "Искомая комбинация слов нигде не встречается"
        time.sleep(3)
        #возвращаемся на главную страницу
        main_page_button = driver.find_element_by_xpath("//img[@alt =\"Official website\"]")
        main_page_button.click()
        time.sleep(5)
        first_page_title = driver.find_element_by_xpath("//h2")
        print(first_page_title.text)
        assert first_page_title.text == "Лучшие предложения"
    finally:
        driver.quit()


# pytest test_sber_main_page.py::test_color_link -v -s -W=ignore