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
    #Пробуем найти это слово в выпадающем списке и видим, что он пуст
    try:
        search_name_button = driver.find_element_by_xpath("//button[text() = \"Кабриолет салатовый\"]")
    except:
        print("Не нашел ничего по поиску \"Кабриолет салатовый\"")

    time.sleep(5)
    #Ищем элемент Закрыть поиск:
    close_search_button = driver.find_element_by_xpath("//button[text()='Закрыть поиск']")
    close_search_button.click()

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