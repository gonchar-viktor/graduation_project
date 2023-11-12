from selenium.webdriver.common.by import By

from helpers.base import BasePage


class HeaderElement(BasePage):
    """
    f
    """

    ALL_PROMOTIONS_LOCATOR = By.XPATH, \
        '//*[@class="styles_promoList__yozMt"]//*[text()="Все акции"]'
    MARKDOWN_LOCATOR = By.XPATH, '//*[text()="Уценка"]'
    TIRES_LOCATOR = By.XPATH, '//*[text()="Шины"]'
    REFRIGERATORS_LOCATOR = By.XPATH, '//*[text()="Холодильники"]'
    WASHING_MACHINES_LOCATOR = By.XPATH, '//*[text()="Стиральные машины"]'
    BOILERS_LOCATOR = By.XPATH, '//*[text()="Котлы"]'
    SMARTPHONES_LOCATOR = By.XPATH, '//*[text()="Смартфоны"]'
    LAPTOPS_LOCATOR = By.XPATH, '//*[text()="Ноутбуки"]'
    TELEVISIONS_LOCATOR = By.XPATH, '//*[text()="Телевизоры"]'
    VACUUM_CLEANERS_LOCATOR = By.XPATH, '//*[text()="Пылесосы"]'
    MATTRESSES_LOCATOR = By.XPATH, '//*[text()="Матрасы"]'
    SOFAS_LOCATOR = By.XPATH, '//*[text()="Диваны"]'






