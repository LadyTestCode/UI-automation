from selenium.webdriver.common.by import By

class BasePageLocators():
    FIRST_TITLE_ON_PAGE = (By.XPATH, "(//h1)[1]")

class MainPageLocators (BasePageLocators):
    EXCHANGE_RATES_LINK = (By.XPATH,"//a[@data-cga_click_extra_link =\"Курсы валют\"]")
    GEOPOSITION_LINK = (By.XPATH,"//a[@title=\"Изменить регион\"]")
    SECOND_TITLE_ON_PAGE = (By.XPATH, "(//h2)[1]")
    REGION_NAME_FIELD = (By.XPATH,"//input[@aria-label=\"Введите имя региона\"]")
    ROSTOV_REGION_FIELD = (By.XPATH,"//button [text()=\"Ростовская область\"]")
    SBERONLINE_LINK = (By.XPATH,"//a[text()=\"СберБанк Онлайн\"]")
    OFFICES_LINK = (By.XPATH,"//a[@data-cga_click_extra_link =\"Курсы валют\"]/following::a[1]")
    ATM_LINK = (By.XPATH,"//a[@data-cga_click_extra_link =\"Курсы валют\"]/following::a[2]")
    OPEN_SEARCH_LINK = (By.XPATH,"//a[@aria-label=\"Открыть поиск по сайту\"]")
    SEARCH_FIELD_LINK = (By.XPATH,"//input[@aria-label=\"Поиск по сайту\"]")
    SEARCH_BUTTON = (By.XPATH, "//button[text()='Найти']")
    SEARCH_SUCCESS_REGION_BUTTON = (By.XPATH, "//button[@class='kitt-header-region__region']")
    SEARCH_RESULTS = (By.XPATH, //input[@type=\"search\" and @placeholder = \"Что-нибудь поищем\"])