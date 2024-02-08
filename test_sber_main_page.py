import PyTest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
#для возможности ожидать загружающийся элемент:
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
#для использования кнопок:
from selenium.webdriver.common.keys import Keys
from pages import locators as locators
from Steps import support_steps as support_steps
#import allure
from pages.main_page import MainPage

#учебный тест для проверки главной страницы
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_elements_sber_main_page(browser):
    with allure.step("Учебный тест для проверки главной страницы"):
        try:
            browser.implicitly_wait(10)
            # Открываем главную страницу
            browser.get("http://www.sberbank.ru/")
            # Раскрываем окно на полный экран
            browser.maximize_window()
            # Ожидаем 5 секунд для прорисовки
            time.sleep(5)
            browser.find_element_by_tag_name("span")
            #browser.find_element_by_id("main-page")
            #browser.find_element_by_css_selector("#main-page > div")
            browser.find_element_by_xpath(locators.SBERONLINE_LINK)
            browser.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/following::div[1]")
            browser.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/following::div[1]/a[1]")
            browser.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]/parent::div[1]")
            browser.find_element_by_xpath(locators.EXCHANGE_RATES_LINK)

            #Домашнее задание - поиск элементов:
            browser.find_element_by_xpath(locators.GEOPOSITION_LINK)
            browser.find_element_by_xpath("//a[text()=\"ENG\"]")
            browser.find_element_by_xpath(locators.OPEN_SEARCH_LINK)

            #Выполнение действий с найденными элементами - и возврат на предыдущую вкладку:
            sberonline_button = browser.find_element_by_xpath(locators.SBERONLINE_LINK)
            sberonline_button.click()
            time.sleep(5)
            browser.switch_to.window(browser.window_handles[0])
            time.sleep(5)

            #button_individ = browser.find_element_by_xpath("//a[text()=\"СберБанк Онлайн\"]")
            #Имитируем наведение мыши для получения всплывающей подсказки
            #ActionChains(browser).move_to_element(button_individ).perform()
            #time.sleep(5)

            geo_button = browser.find_element_by_xpath(locators.GEOPOSITION_LINK)
            print("geo_button =", geo_button.text)
            geo_button.click()
            region_name_field = browser.find_element_by_xpath("//input[@aria-label=\"Введите имя региона\"]")
            region_name_field.send_keys("Какая-то область")
            time.sleep(2)
            region_name_field.clear()
            time.sleep(2)
            region_name_field.send_keys("Ростовская область")
            region_name_button = browser.find_element_by_xpath(locators.ROSTOV_REGION_FIELD)
            region_name_button.click()
            time.sleep(5)

            #Ожидаем доступности элемента и только потом нажимаем на него:
            button = WebbrowserWait(browser, 15).until(EC.element_to_be_clickable((By.XPATH, locators.GEOPOSITION_LINK)))
            button.click()

            #Прокрутим страницу вниз:
            browser.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(5)
        finally:
            browser.quit()

#тест - проверка наведения курсора мыши на объект
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_mouse_over_menu(browser):
    with allure.step("Tест - проверка наведения курсора мыши на объект"):
        try:
            browser.implicitly_wait(10)
            # Открываем главную страницу
            browser.get("http://www.sberbank.ru/")
            # Раскрываем окно на полный экран
            browser.maximize_window()
            # Ожидаем 5 секунд для прорисовки
            time.sleep(5)
            # Имитируем наведение мыши на элементы - 3 задание домашней работы:
            button_cources = browser.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]")
            ActionChains(browser).move_to_element(button_cources).perform()
            time.sleep(5)

            button_offices = browser.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]/following::a[1]")
            ActionChains(browser).move_to_element(button_offices).perform()
            time.sleep(5)

            button_atm = browser.find_element_by_xpath("//a[@data-cga_click_extra_link =\"Курсы валют\"]/following::a[2]")
            ActionChains(browser).move_to_element(button_atm).perform()
            time.sleep(5)

            button_geo = browser.find_element_by_xpath(locators.GEOPOSITION_LINK)
            ActionChains(browser).move_to_element(button_geo).perform()
            time.sleep(5)

            button_language = browser.find_element_by_xpath("//a[text()=\"ENG\"]")
            ActionChains(browser).move_to_element(button_language).perform()
            time.sleep(5)

            button_search = browser.find_element_by_xpath(locators.OPEN_SEARCH_LINK)
            ActionChains(browser).move_to_element(button_search).perform()
            time.sleep(5)
        finally:
            browser.quit()


# тест проверяет переключения на английский язык
@pytest.mark.full_regression
@pytest.mark.smoke_regression
def test_change_language_sber_main_page(browser):
    with allure.step("Тест проверяет переключения на английский язык"):
        try:
            browser.implicitly_wait(10)
            # Открываем главную страницу
            browser.get("http://www.sberbank.ru/")
            # Раскрываем окно на полный экран
            browser.maximize_window()
            # Ожидаем 5 секунд для прорисовки
            time.sleep(5)
            language_button = browser.find_element_by_xpath("//a[text()=\"ENG\"]")
            language_button.click()
            time.sleep(5)
        finally:
            browser.quit()

# тест проверяет поиск по слову Кредит и отсутствие вариантов поиска по сочетанию Кабриолет салатовый
@pytest.mark.full_regression
@pytest.mark.smoke_regression
def test_check_search_sber_main_page(browser):
    with allure.step("Тест проверяет поиск по слову Кредит и отсутствие вариантов поиска по сочетанию Кабриолет салатовый"):
        try:
            browser.implicitly_wait(10)
            # Открываем главную страницу
            browser.get("http://www.sberbank.ru/")
            # Раскрываем окно на полный экран
            browser.maximize_window()
            # Ожидаем 5 секунд для прорисовки
            time.sleep(5)
            search_element= browser.find_element_by_xpath(locators.OPEN_SEARCH_LINK)
            search_element.click();
            time.sleep(5)
            #открываем поисковую строку
            search_field = browser.find_element_by_xpath(locators.SEARCH_FIELD_LINK)
            search_field.send_keys("Кредит")
            time.sleep(5)
            #Нажимаем Найти и видим результаты поиска
            search_button = browser.find_element_by_xpath("//button[text()='Найти']")
            search_button.click()
            time.sleep(5)
            #кликаем в поле ввода условий поиска
            search_element = browser.find_element_by_xpath(locators.OPEN_SEARCH_LINK)
            search_element.click();
            #осуществляем новый поиск
            search_field = browser.find_element_by_xpath(locators.SEARCH_FIELD_LINK)
            search_field.send_keys("Кабриолет салатовый")
            time.sleep(5)
            #Пробуем найти это слово в выпадающем списке и видим, вариантов нужных нет
            search_name_button = browser.find_elements_by_xpath("//button[text() = \"Кабриолет салатовый\"]")
            assert len(search_name_button) == 0
            time.sleep(5)
            #Ищем элемент Закрыть поиск:
            close_search_button = browser.find_element_by_xpath("//button[text()='Закрыть поиск']")
            close_search_button.click()
            #Реализуем подсчет элементов, удовлетворяющих условию поиска:
            exchange_rates_count = browser.find_elements_by_xpath(locators.EXCHANGE_RATES_LINK)
            print("count курсы валют =", len(exchange_rates_count))

            #Посчитаем количество элементов Офисы и Банкоматы
            offices_rates_count = browser.find_elements_by_xpath(locators.OFFICES_LINK)
            print("count офисы =", len(offices_rates_count))
            bankomates_rates_count = browser.find_elements_by_xpath(loators.ATM_LINK)
            print("count банкоматы =", len(bankomates_rates_count))
        finally:
            browser.quit()

#Домашнее задание: тест  на проверку скроллинга и переключения между вкладками.
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_change_tab_and_scroll(browser):
    with allure.step("Домашнее задание: тест  на проверку скроллинга и переключения между вкладками."):
        try:
            browser.implicitly_wait(10)
            # Открываем главную страницу
            browser.get("http://www.sberbank.ru/")
            # Раскрываем окно на полный экран
            browser.maximize_window()
            # Ожидаем 5 секунд для прорисовки
            time.sleep(5)
            sberonline_button = browser.find_element_by_xpath(locators.SBERONLINE_LINK)
            sberonline_button.click()
            time.sleep(5)
            #из новой открытой вкладки возвращаемся в исходную
            browser.switch_to.window(browser.window_handles[0])
            time.sleep(5)
            #затем снова в новую вкладку и снова возвращеаемся назад:
            browser.switch_to.window(browser.window_handles[1])
            time.sleep(5)
            browser.switch_to.window(browser.window_handles[0])
            time.sleep(5)
            #скролл вниз на один экран
            browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
            time.sleep(5)
            #скролл вниз до футера
            browser.find_element_by_tag_name('body').send_keys(Keys.END)
            time.sleep(5)
            #скролл вверх на один экран
            browser.find_element_by_tag_name('body').send_keys(Keys.PAGE_UP)
            time.sleep(5)
            #скрол вверх до хедера
            browser.find_element_by_tag_name('body').send_keys(Keys.HOME)
            time.sleep(5)
        finally:
            browser.quit()

# тест проверки выбора геолокации
@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize ('text',
    ["Санкт-Петербург"
    "Ростовская",
    "Республика Ca",
    "Адыгея"
    "сахалин",
    "кРасНоДар"],
    ids=("City", "Region", "Part og region", "Region name", "Low letters", "Crazy letters")
    )
def test_check_geoposition(browser, text):
   # with allure.step("Домашнее задание: тест  на проверку скроллинга и переключения между вкладками."):
   main_page = MainPage(browser,"http://www.sberbank.ru/")
   # Открываем тестовую страницу
   main_page.open()
   # Нажимаем на ссылку геопозиции
   main_page.click_on_geoposition_link()
   # Вводим название региона
   main_page.fill_text_region_name_field(text)
   # Нажимаем на ссылку названия региона
   main_page.click_on_region_name_link(text)
   # Проверяем, что регион корректно выбран
   main_page.assert_region_name_in_geo_link(text)

#тест для проверки ввода некорректно введенной геолокации
@pytest.mark.full_regression
def test_incorrect_geoposition(browser):
    main_page = MainPage(browser, "http://www.sberbank.ru/")
    # Открываем тестовую страницу
    main_page.open()
    # Нажимаем на ссылку геопозиции
    main_page.click_on_geoposition_link()
    # Вводим некорректное значение в поиск
    main_page.fill_incorrect_text_region_name_field()
    # Проверяем, что поиск пустой
    main_page.should_not_be_search_success_region_button()

#тест для проверки перехода по ссылке меню - пробный кейс - не для запуска и проверки!
@pytest.mark.full_regression
def test_moving_menu_links_test(browser):
    with allure.step("Тест для проверки перехода по ссылке меню - пробный"):
        try:
            # Запуск браузера
            chrome_options = webbrowser.ChromeOptions()
            chrome_options.add_argument("--disable-notifications")
            browser = webbrowser.Chrome(chrome_options = chrome_options, executable_path=r'/Users/20071554/Downloads/SberBrowserbrowser_9.2.36.0-macos')
            browser.implicitly_wait(15)
            browser.maximize_window()
            browser.get('https://www.sberbank.ru/')
            exchange_rates_button = browser.find_element_by_xpath("(//a[text()=\"Курсы валют\"])[1]")
            exchange_rates_button.click()
            time.sleep(5)
            first_page_title = browser.find_element_by_xpath("//h1")
            assert first_page_title.text == "Курсы валют"
            time.sleep(3)
        finally:
            browser.quit()

#тест для проверки перехода по ссылкам - открытие правильной страницы - курсы валют
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_moving_menu_links_exchange(browser):
    with allure.step("Тест для проверки перехода по ссылке меню - пробный"):
        main_page = MainPage(browser, "http://www.sberbank.ru/")
        # Открываем тестируемую страницу
        main_page.open()
        # Убедимся, что ссылка на курсы валют присутствует
        main_page.should_be_exchange_rates_link()
        # Находим ссылку курсов валют и нажимаем на нее
        main_page.click_on_exchange_rates_link()
        # Проверяем, что мы перешли на нужную страницу
        main_page.assert_exchange_rates_title()

#тест для проверки перехода по ссылкам - открытие правильной страницы - офисы
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_moving_menu_links_offices(browser):
    with allure.step("Тест для проверки перехода по ссылкам - открытие правильной страницы - офисы"):
        main_page = MainPage(browser, "http://www.sberbank.ru/")
        # Открываем тестируемую страницу
        main_page.open()
        # Убедимся, что ссылка на офисы присутствует
        main_page.should_be_offices_link()
        # Находим ссылку Офисы и нажимаем на нее
        main_page.click_on_offices_link()
        # Проверяем, что мы перешли на нужную страницу
        main_page.assert_offices_title()

#тест для проверки перехода по ссылкам - открытие правильной страницы - сбербанк онлайн
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_moving_menu_links_sbol(browser):
    with allure.step("Тест для проверки перехода по ссылкам - открытие правильной страницы - сбербанк онлайн"):
       main_page = MainPage(browser, "http://www.sberbank.ru/")
       # Открываем тестируемую страницу
       main_page.open()
       # Убедимся, что ссылка на sberbank online присутствует
       main_page.should_be_sberbankonline_link()
       # Находим ссылку sberbank online и нажимаем на нее
       main_page.click_on_sberbankonline_link()
       # Проверяем, что мы перешли на нужную страницу
       main_page.assert_sberbankonline_title()

#тест для проверки перехода по ссылкам - открытие правильной страницы -банкоматы
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_moving_menu_links_atm(browser):
    with allure.step("Тест для проверки перехода по ссылкам - открытие правильной страницы -банкоматы"):
        main_page = MainPage(browser, "http://www.sberbank.ru/")
        # Открываем тестируемую страницу
        main_page.open()
        # Убедимся, что ссылка на банкоматы присутствует
        main_page.should_be_atm_link()
        # Находим ссылку Банкоматы  и кликаем на нее
        main_page.click_on_atm_link()
        # Проверяем, что мы перешли на нужную страницу
        main_page.assert_atm_title()


#тест подсчета элементов на странице
@pytest.mark.full_regression
@pytest.mark.smoke_regression
def test_count_links(browser):
    with allure.step("Тест подсчета элементов на странице"):
        main_page = MainPage(browser, "http://www.sberbank.ru/")
        # Открываем тестируемую страницу
        main_page.open()
        #Проверим количество найденных элементов - ссылок на Обмен валют
        main.page.assert_count_exchange_is_correct()
        #Проверим количество найденных элементов - ссылок на "СберБанк Онлайн".
        main.page.assert_count_sberonline_is_correct()
        # Проверим количество найденных элементов - ссылок на Офисы
        main.page.assert_count_offices_is_correct()
        # Проверим количество найденных элементов - ссылок на Банкоматы
        main.page.assert_count_atm_is_correct()


#тест для проверки изменения цвета ссылок при наведении мыши
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_color_link(browser):
    with allure.step("Изменение цвета ссылок"):
        main_page = MainPage(browser, "http://www.sberbank.ru/")
        # Отрываем тестируемую страницу
        main_page.open()
        # Убедимся, что ссылка на sberbank online присутствует
        main_page.should_be_sberbankonline_link()
        # Находим ссылку sberbank online и после наведения мыши проверям ее цвет
        main_page.check_color_of_sberbankonline_link()
        # Убедимся, что ссылка на курсы валют присутствует
        main_page.should_be_exchange_rates_link()
        # Находим ссылку курсы валют и после наведения мыши проверям ее цвет
        main_page.check_color_of_exchange_rates_link()
        # Убедимся, что ссылка на Офисы присутствует
        main_page.should_be_offices_link()
        # Находим ссылку Офисы и после наведения мыши проверям ее цвет
        main_page.check_color_of_offices_link()
        # Убедимся, что ссылка на Банкоматы присутствует
        main_page.should_be_atm_link()
        # Находим ссылку Банкоматы и после наведения мыши проверям ее цвет
        main_page.check_color_of_atm_link()


#Тест с проверками корректности заголовков страниц для сценария перехода между страницами
@pytest.mark.smoke_regression
@pytest.mark.full_regression
def test_correctness_of_headers_for_pages(browser):
    with allure.step("Тест с проверками корректности заголовков страниц для сценария перехода между страницами"):
        main_page = MainPage(browser, "http://www.sberbank.ru/")
        # Отрываем тестируемую страницу
        main_page.open()
        # Убедимся, что мы на главной странице - по тексту заголовка
        main_page.assert_main_page_title()
        # Убедимся, что ссылка на sberbank online присутствует
        main_page.should_be_sberbankonline_link()
        # Находим ссылку sberbank online и нажимаем на нее
        main_page.click_on_sberbankonline_link()
        # Проверяем, что мы перешли на нужную страницу
        main_page.assert_sberbankonline_title()
        #из новой открытой вкладки возвращаемся в исходную
        browser.switch_to.window(browser.window_handles[0])
        time.sleep(5)
        #проверяем, что это главная страница
        main_page.assert_main_page_title()

# тест проверяет корректность работы поиска
@pytest.mark.smoke_regression
@pytest.mark.full_regression
@pytest.mark.parametrize ('searchtext',
    [("Вклад",1),
     ("Кредит",1),
     ("Чертополох",0),
     ("ВкЛаД",1),
     ("Exchange",0)],
    ids=("correct", "correct", "incorrect", "Low and up letters", "English letters")
    )
def test_check_correct_search_sber_main_page(browser, text):
    with allure.step("Тест проверяет корректность работы поиска"):
        main_page = MainPage(browser, "http://www.sberbank.ru/")
        # Отрываем тестируемую страницу
        main_page.open()
        # Убедимся, что ссылка на поиск присутствует
        main_page.should_be_search_link()
        # Находим ссылку поиска и нажимаем на нее
        main_page.click_on_search_link()
        time.sleep(5)
        # Проверяем, что открылось окно поиска()
        main_page.assert_search_field_title()
        # открываем поисковую строку и вводим слово из параметров для поиска и нажимаем кнопку найти
        main_page.click_on_search_field_link()
        main_page.write_word_in_search_field(seachtext)
        main_page.click_on_search_button()
        time.sleep(5)
        main_page.assert_search_is_successfull()

                    #Убеждаемся, что мы перешли на страницу поиска
                    search_page_fields = browser.find_elements_by_xpath("//input[@type=\"search\" and @placeholder = \"Что-нибудь поищем\"]")
                    assert len(search_page_fields) >=1
                    #Проверим, что какие то результаты по нашему поиску есть
                    search_results = browser.find_elements_by_xpath("//yass-span")
                    assert len(search_results) >= 1
        #Пробуем найти чертополох и убждаемся, что корректно обрабатываются пустые результаты поиска
        search_page_field = browser.find_element_by_xpath("//input[@type=\"search\" and @placeholder = \"Что-нибудь поищем\"]")
        search_page_field.clear()
        search_page_field.send_keys("Чертополох")
        #ищем и нажимаем кнопку поиска
        search_button = browser.find_element_by_xpath("//input[@type=\"button\"]")
        search_button.click()
        time.sleep(3)
        incorrect_search_results = browser.find_element_by_xpath("(//yass-div)[4]")
        print(incorrect_search_results.text)
        assert incorrect_search_results.text == "Искомая комбинация слов нигде не встречается"
        time.sleep(3)
        #возвращаемся на главную страницу
        main_page_button = browser.find_element_by_xpath("//img[@alt =\"Official website\"]")
        main_page_button.click()
        time.sleep(5)
        first_page_title = browser.find_element_by_xpath("//h2")
        print(first_page_title.text)
        assert first_page_title.text == "Лучшие предложения"



# PyTest test_sber_main_page.py::test_color_link -v -s -W=ignore --bro=IE
# pytest -m smoke_regression