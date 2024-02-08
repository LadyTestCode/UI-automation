from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    #--------------------Главная страница--------
    #Проверка заголовка главной страницы
    def assert_main_page_title(self):
        assert self.driver.find_element(*MainPageLocators.SECOND_TITLE_ON_PAGE).text == "Лучшие предложения", "Возможно, мы не на главной странице"

    #Ищем кнопку Поиск и нажимаем на нее
    def should_be_search_link(self):
        button_search = self.driver.find_element(*MainPageLocators.OPEN_SEARCH_LINK)
        button_search.click()

    #Проверим, что открылось окно поиска
    def assert_search_field_title(self):
        assert self.driver.find_element(*MainPageLocators.SEARCH_FIELD_LINK), "Окно поиска не открылось"

    # Кликаем на окно поиска
    def click_on_search_field_link(self):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_FIELD_LINK)
        search_field.click()

    #Вводим слово для поиска
    def write_word_in_search_field(self, searchword):
        search_field = self.driver.find_element_by_xpath(locators.SEARCH_FIELD_LINK)
        search_field.clear()
        search_field.send_keys(searchword)

    def click_on_search_button(self):
        search_field = self.driver.find_element(*MainPageLocators.SEARCH_BUTTON)
        search_field.click()

    # Убеждаемся, что мы перешли на страницу поиска и смотрим, что было найдено
    def assert_search_is_successfull():
        search_page_fields = browser.find_elements_by_xpath("//input[@type=\"search\" and @placeholder = \"Что-нибудь поищем\"]")
        assert len(search_page_fields) >= 1
        # Проверим, что какие то результаты по нашему поиску есть
        search_results = browser.find_elements_by_xpath("//yass-span")
        assert len(search_results) >= 1

    #------------------КУРСЫ ВАЛЮТ---------------
    #Проверим, что есть ссылка Курсы валют
    def should_be_exchange_rates_link(self):
        assert self.is_element_present(*MainPageLocators.EXCHANGE_RATES_LINK), "Ссылка \"Курсы валют\" отсутствует"

    #Нажмем на ссылку Курсы валют
    def click_on_exchange_rates_link(self):
        button = self.driver.find_element(*MainPageLocators.EXCHANGE_RATES_LINK)
        button.click()

    #Проверим, что название открывшейся страницы Курсы валют
    def assert_exchange_rates_title(self):
        assert self.driver.find_element(*MainPageLocators.FIRST_TITLE_ON_PAGE).text == "Курсы валют", "Первый заголовок не Курсы валют"

    #Проверим, что ссылка Курсы валют после наведения мыши меняет свой цвет
    def check_color_of_sberbankonline_link(self):
        check_color_of_visited_link(self, *MainPageLocators.EXCHANGE_RATES_LINK)

    #Ищем количество заданных элементов
    def assert_count_exchange_is_correct(self):
        assert_count_of_elements_is_correct(*MainPageLocators.EXCHANGE_RATES_LINK, 4)


    #----------------------ОФИСЫ-------------------
    #Проверим, что есть ссылка Офисы
    def should_be_offices_link(self):
        assert self.is_element_present(*MainPageLocators.OFFICES_LINK), "Ссылка \"Офисы\" отсутствует"

    #Нажмем на ссылку Офисы
    def click_on_offices_link(self):
        button = self.driver.find_element(*MainPageLocators.OFFICES_LINK)
        button.click()

    #Проверим, что название открывшейся страницы Офисы и банкоматы
    def assert_offices_title(self):
        assert self.driver.find_element(*MainPageLocators.FIRST_TITLE_ON_PAGE).text == "Офисы и банкоматы", "Первый заголовок не Офисы и банкоматы"

    # Проверим, что ссылка Офисы после наведения мыши меняет свой цвет
    def check_color_of_offices_link(self):
        check_color_of_visited_link(self,*MainPageLocators.OFFICES_LINK)

    # Ищем количество заданных элементов
    def assert_count_offices_is_correct(self):
        assert_count_of_elements_is_correct(*MainPageLocators.OFFICES_LINK, 3)

#----------------------СБЕРБАНК ОНЛАЙН-------------------
    #Проверим, что есть ссылка на сбербанк онлайн
    def should_be_sberbankonline_link(self):
        assert self.is_element_present(*MainPageLocators.SBERONLINE_LINK), "Ссылка \"Сбербанк онлайн\" отсутствует"

    #Нажмем на ссылку сбербанк онлайн
    def click_on_sberbankonline_link(self):
        button = self.driver.find_element(*MainPageLocators.SBERONLINE_LINK)
        button.click()

    #Проверим, что название открывшейся страницы - сбербанк онлайн
    def assert_sberbankonline_title(self):
        assert self.driver.find_element(*MainPageLocators.FIRST_TITLE_ON_PAGE).text == "Сбербанк онлайн", "Первый заголовок не Сбербанк Онлайн"

    # Проверим, что ссылка СБОЛ после наведения мыши меняет свой цвет
    def check_color_of_sberbankonline_link(self):
        check_color_of_visited_link(self, *MainPageLocators.SBERONLINE_LINK)

    #Ищем количество заданных элементов
    def assert_count_exchange_is_correct(self):
        assert_count_of_elements_is_correct(*MainPageLocators.SBERONLINE_LINK, 1)

#----------------------БАНКОМАТЫ-------------------
    #Проверим, что есть ссылка Банкоматы
    def should_be_atm_link(self):
        assert self.is_element_present(*MainPageLocators.ATM_LINK), "Ссылка \"Банкоматы\" отсутствует"

    #Нажмем на ссылку Офисы
    def click_on_atm_link(self):
        button = self.driver.find_element(*MainPageLocators.ATM_LINK)
        button.click()

    #Проверим, что название открывшейся страницы Офисы и банкоматы
    def assert_atm_title(self):
        assert self.driver.find_element(*MainPageLocators.FIRST_TITLE_ON_PAGE).text == "Офисы и банкоматы", "Первый заголовок не Офисы и банкоматы"

    # Проверим, что ссылка Банкоматы после наведения мыши меняет свой цвет
    def check_color_of_sberbankonline_link(self):
        check_color_of_visited_link(self, *MainPageLocators.ATM_LINK)

        # Ищем количество заданных элементов
    def assert_count_atm_is_correct(self):
        assert_count_of_elements_is_correct(*MainPageLocators.ATM_LINK, 3)

#----------------------------УПРАВЛЕНИЕ ГЕОПОЗИЦИЕЙ----------
    def click_on_geoposition_ink(self):
        link = self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK)
        link.click()

    def click_on_region_name_link(self, text):
        link = self.driver.find_element(By.XPATH, "//button[text()[contains(.,'" + text.title() + "')]]")
        link.click()

    def fill_text_region_name_field(self, text):
        self.driver.find_element(*MainPageLocators.REGION_NAME_FIELD).send_Keys(text)

    def fill_incorrect_text_region_name_field(self):
        self.driver.find_element(*MainPageLocators.REGION_NAME_FIELD).send_Keys("abracadabra")

    def assert_region_name_in_geo_link(self, text):
        assert self.driver.find_element(*MainPageLocators.GEOPOSITION_LINK).text.__contains__(text.title()), "Регион B гео не найден"

    def should_not_be_search_success_region_button(self):
        assert self.is_not_element_present(*MainPageLocators.SEARCH_SUCCESS_REGION_BUTTON), "Заданный злемент присутствует"

    #-----------------------COMMON FUNCTIONS-----------------------
    def check_color_of_visited_link(self, linklocator):
        link_button = self.driver.find_element(linklocator)
        color_before_perform = link_button.value_of_css_property("color")
        ActionChains(driver).move_to_element(link_button).perform()
        color_after_perform = link_button.value_of_css_property("color")
        assert color_before_perform != color_after_perform, "Ссылка не изменила цвет"

    def assert_count_of_elements_is_correct(self, linklocator, number):
        assert len(self.driver.find_elements_by_xpath(linklocator)) == number
