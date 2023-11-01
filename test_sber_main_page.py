import pytest
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

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

    #Выполнение действий с найденными элементами:
    sberonline_button = driver.find_element_by_xpath("//a[text()='СберБанк Онлайн']")
    sberonline_button.click()