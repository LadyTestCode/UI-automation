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

def test_elements_sber_main_page():
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
    driver.find_element_by_xpath("//a[text()='СберБанк Онлайн']")
    driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/following::div[1]")
    driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/following::div[1]/a[1]")
    driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/parent::div[1]")
    driver.find_element_by_xpath("(//a[text()=\"Курсы валют\"]) [1]")

    #Домашнее задание - поиск элементов:
    driver.find_element_by_xpath("//a[@title=\"Изменить регион\"]")
    driver.find_element_by_xpath("//a[text()=\"ENG\"]")
    driver.find_element_by_xpath("//a[@aria-label=\"Открыть поиск по сайту\"]")

    #Выполнение действий с найденными элементами - и возврат на предыдущую вкладку:
    sberonline_button = driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
    sberonline_button.click()
    time.sleep(5)
    driver.switch_to.window(driver.window_handles[0])
    time.sleep(5)

    #button_individ = driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
    #Имитируем наведение мыши для получения всплывающей подсказки
    #ActionChains(driver).move_to_element(button_individ).perform()
    #time.sleep(5)

    geo_button = driver.find_element_by_xpath("//a[@title=\"Изменить регион\"]")
    print("geo_button =", geo_button.text)
    geo_button.click()
    region_name_field = driver.find_element_by_xpath("//input[@aria-label=\"Введите имя региона\"]")
    region_name_field.send_keys("Какая-то область")
    time.sleep(2)
    region_name_field.clear()
    time.sleep(2)
    region_name_field.send_keys("Ростовская область")
    region_name_button = driver.find_element_by_xpath("//button[text() = \"Ростовская область\"]")
    region_name_button.click()
    time.sleep(5)

    # Имитируем наведение мыши на элементы - 3 задание домашней работы:
    button_cources = driver.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]")
    ActionChains(driver).move_to_element(button_cources).perform()
    time.sleep(5)

    button_offices = driver.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]/following::a[1]")
    ActionChains(driver).move_to_element(button_offices).perform()
    time.sleep(5)

    button_bankomats = driver.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]/following::a[2]")
    ActionChains(driver).move_to_element(button_bankomats).perform()
    time.sleep(5)

    button_geo = driver.find_element_by_xpath("//a[@title=\"Изменить регион\"]")
    ActionChains(driver).move_to_element(button_geo).perform()
    time.sleep(5)

    button_language = driver.find_element_by_xpath("//a[text()=\"ENG\"]")
    ActionChains(driver).move_to_element(button_language).perform()
    time.sleep(5)

    button_search = driver.find_element_by_xpath("//a[@aria-label=\"Открыть поиск по сайту\"]")
    ActionChains(driver).move_to_element(button_search).perform()
    time.sleep(5)

    #Ожидаем доступности элемента и только потом нажимаем на него:
    button = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//a[@title=\"Изменить регион\"]")))
    button.click()

    #Прокрутим страницу вниз:
    driver.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(5)

# тест проверяет переключения на английский язык
def test_change_language_sber_main_page():
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

# тест проверяет поиск по слову Кредит и отсутствие вариантов поиска по сочетанию Кабриолет салатовый
def test_check_search_sber_main_page():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    # Открываем главную страницу
    driver.get("http://www.sberbank.ru/")
    # Раскрываем окно на полный экран
    driver.maximize_window()
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    search_element= driver.find_element_by_xpath("//a[@aria-label=\"Открыть поиск по сайту\"]")
    search_element.click();
    time.sleep(5)
    #открываем поисковую строку
    search_field = driver.find_element_by_xpath("//input[@aria-label=\"Поиск по сайту\"]")
    search_field.send_keys("Кредит")
    time.sleep(5)
    #Нажимаем Найти и видим результаты поиска
    search_button = driver.find_element_by_xpath("//button[text()='Найти']")
    search_button.click()
    time.sleep(5)

    search_element = driver.find_element_by_xpath("//a[@aria-label=\"Открыть поиск по сайту\"]")
    search_element.click();
    search_field = driver.find_element_by_xpath("//input[@aria-label=\"Поиск по сайту\"]")
    search_field.send_keys("Кабриолет салатовый")
    time.sleep(5)
    #Пробуем найти это слово в выпадающем списке и видим, вариантов нужных нет
    try:
        search_name_button = driver.find_element_by_xpath("//button[text() = \"Кабриолет салатовый\"]")
    except:
        print("Не нашел ничего по поиску \"Кабриолет салатовый\"")
    time.sleep(5)
    #Ищем элемент Закрыть поиск:
    close_search_button = driver.find_element_by_xpath("//button[text()='Закрыть поиск']")
    close_search_button.click()
    #Реализуем подсчет элементов, удовлетворяющих условию поиска:
    exchange_rates_count = driver.find_elements_by_xpath("//a[text()=\"Курсы валют\"]")
    print("count курсы валют =", len(exchange_rates_count))

    #Посчитаем количество элементов Офисы и Банкоматы
    offices_rates_count = driver.find_elements_by_xpath("//a[text()=\"Офисы\"]")
    print("count офисы =", len(offices_rates_count))
    bankomates_rates_count = driver.find_elements_by_xpath("//a[text()=\"Банкоматы\"]")
    print("count банкоматы =", len(bankomates_rates_count))

#Домашнее задание: тест  на проверку скроллинга и переключения между вкладками.
def test_change_tab_and_scroll():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    # Открываем главную страницу
    driver.get("http://www.sberbank.ru/")
    # Раскрываем окно на полный экран
    driver.maximize_window()
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    sberonline_button = driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
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

# тест проверки выбора геолокации
def test_check_geopostion():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    geo_button = driver.find_element_by_xpath("//a[@title=\"Изменить регион\"]")
    geo_button.click()
    region_name_field = driver.find_element_by_xpath("//input[@aria-label=\"Введите имя региона\"]")
    region_name_field.send_keys("Ростовская область")
    region_name_button = driver.find_element_by_xpath("//button [text()=\"Ростовская область\"]")
    region_name_button.click()
    geo_button = driver.find_element_by_xpath("//a[@title=\"Изменить регион\"]")
    assert geo_button.text == "Ростовская область"

#---------------------------------- Home work -------------------

#тест для проверки перехода по ссылкам - открытие правильной страницы - курсы валют
def test_moving_menu_links_exchange():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    exchange_rates_button = driver.find_element_by_xpath("//a[text()=\"Курсы валют\"]")
    exchange_rates_button.click()
    first_page_title = driver.find_element_by_xpath ("(//h1)[1]")
    assert first_page_title.text == "Курсы валют"

#тест для проверки перехода по ссылкам - открытие правильной страницы - офисы
def test_moving_menu_links_offices():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    offices_rates_button = driver.find_element_by_xpath("//a[text()=\"Офисы\"]")
    offices_rates_button.click()
    first_page_title = driver.find_element_by_xpath ("(//h1) [1]")
    assert first_page_title.text == "Офисы и банкоматы"

#тест для проверки перехода по ссылкам - открытие правильной страницы - сбербанк онлайн
def test_moving_menu_links_sbol():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    sbol_rates_button = driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
    sbol_rates_button.click()
    first_page_title = driver.find_element_by_xpath("//h1")
    assert first_page_title.text == "СберБанк"

#тест для проверки перехода по ссылкам - открытие правильной страницы -банкоматы
def test_moving_menu_links_boxes():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    boxes_rates_button = driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
    boxes_rates_button.click()
    first_page_title = driver.find_element_by_xpath ("(//h1) [1]")
    assert first_page_title.text == "Офисы и банкоматы"

#тест подсчета элементов на странице
def test_count_links():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    exchange_rates_count = driver.find_elements_by_xpath("//a[text()=\"Курсы валют\"]")
    print("count курсы валют =", len(exchange_rates_count))
    assert len(exchange_rates_count) == 4
    #далее проверим для остальных элементов: "Офисы", "Банкоматы", "СберБанк Онлайн".

    sberonline_rates_count = driver.find_elements_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
    print("count сбер онлайн =", len(sberonline_rates_count))
    assert len(sberonline_rates_count) == 1

    offices_rates_count = driver.find_elements_by_xpath("//a[text()=\"Офисы\"]")
    print("count офисы =", len(offices_rates_count))
    assert len(offices_rates_count) == 3

    boxes_rates_count = driver.find_elements_by_xpath("//a[text()=\"Банкоматы\"]")
    print("count офисы =", len(boxes_rates_count))
    assert len(boxes_rates_count) == 3


#тест для проверки изменения цвета ссылок при наведении мыши
def test_color_link():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    sberonline_button = driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
    color_before_perform = sberonline_button.value_of_css_property("color")
    ActionChains(driver).move_to_element(sberonline_button).perform()
    color_after_perform = sberonline_button.value_of_css_property("color")
    assert color_before_perform != color_after_perform

#проверим остальные ссылки: "Курсы валют", "Офисы", "Банкоматы".
    exchange_button = driver.find_element_by_xpath("//a[text ()=\"Курсы валют\"]")
    color_before_perform = exchange_button.value_of_css_property("color")
    ActionChains(driver).move_to_element(exchange_button).perform()
    color_after_perform = exchange_button.value_of_css_property("color")
    assert color_before_perform != color_after_perform

    offices_button = driver.find_element_by_xpath("//a[text ()=\"Офисы\"]")
    color_before_perform = offices_button.value_of_css_property("color")
    ActionChains(driver).move_to_element(offices_button).perform()
    color_after_perform = offices_button.value_of_css_property("color")
    assert color_before_perform != color_after_perform

    boxes_button = driver.find_element_by_xpath("//a[text ()=\"Банкоматы\"]")
    color_before_perform = boxes_button.value_of_css_property("color")
    ActionChains(driver).move_to_element(boxes_button).perform()
    color_after_perform = boxes_button.value_of_css_property("color")
    assert color_before_perform != color_after_perform

#Тест с проверками корректности заголовков страниц для сценария перехода между страницами
def test_correctness_of_headers_for_pages():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    driver.get("http://www.sberbank.ru/")
    driver.maximize_window()
    first_page_title = driver.find_element_by_xpath("//h2")
    print(first_page_title.text)
    assert first_page_title.text == "Лучшие предложения"
    #находим ссылку и переходим на страницу Сбербанк Онлайн
    sberonline_button = driver.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
    sberonline_button.click()
    new_page_title = driver.find_element_by_xpath("//h1")
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

# тест проверяет корректность работы поиска
def test_check_search_sber_main_page():
    driver = webdriver.Chrome('/Users/20071554/Downloads/SberBrowserDriver_9.2.36.0-macos')
    driver.implicitly_wait(10)
    # Открываем главную страницу
    driver.get("http://www.sberbank.ru/")
    # Раскрываем окно на полный экран
    driver.maximize_window()
    # Ожидаем 5 секунд для прорисовки
    time.sleep(5)
    search_element= driver.find_element_by_xpath("//a[@aria-label=\"Открыть поиск по сайту\"]")
    search_element.click();
    time.sleep(5)
    #открываем поисковую строку и вводим слово Вклад для поиска
    search_field = driver.find_element_by_xpath("//input[@aria-label=\"Поиск по сайту\"]")
    search_field.send_keys("Вклад")
    time.sleep(5)
    #Нажимаем Найти
    search_button = driver.find_element_by_xpath("//button[text()='Найти']")
    search_button.click()
    time.sleep(5)
    #Убеждаемся, что мы перешли на страницу поиска
    search_page_title = driver.find_elements_by_xpath("//input[@type=\"search\" and @placeholder = \"Что-нибудь поищем\"]")
    assert len(search_page_title) >=1
    #возвращаемся на главную страницу
    main_page_button = driver.find_element_by_xpath("// img[@alt = \"Official website\"]")
    main_page_button.click()
    time.sleep(5)
    first_page_title = driver.find_element_by_xpath("//h2")
    print(first_page_title.text)
   # assert first_page_title.text == "Лучшие предложения"

# pytest test_sber_main_page.py::test_color_link -v -s -W=ignore