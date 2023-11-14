from selenium.webdriver.common.by import By


class HeaderLocators:

    # react line

    ALL_PROMOTIONS_LOCATOR = (
        By.XPATH, '//*[@class="styles_promoList__yozMt"]//*[text()="'
                  'Все акции"]'
    )
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

    # product categories

    PRODUCT_CATALOG_BUTTON_LOCATOR = (
        By.CSS_SELECTOR, '[class="styles_catalogButton__z9L_j"]'
    )
    CATEGORIES_CONTAINER_LOCATOR = (
        By.CSS_SELECTOR, '[class="styles_categoriesContainer__Nijol"]'
    )

    # city selection

    CITY_SELECTION_BUTTON_LOCATOR = (
        By.CSS_SELECTOR, '[class="styles_localityBtn__qrGFQ"]'
    )
    INPUT_CITY_SELECTION_LOCATOR = (
        By.CSS_SELECTOR, 'input[label="Населенный пункт"]'
    )
    SAVE_BUTTON_LOCATOR = (
        By.CSS_SELECTOR,
        'button[class*="style_baseActionButtonMargin__4haYC"]'
    )
    CONFIRM_CITY_LOCATOR = (
        By.CSS_SELECTOR, 'li[class*="styles_flexRow__oouUy"]'
    )

    # catalog search

    CATALOG_SEARCH_LOCATOR = By.ID, 'catalogSearch'
    CHOOSE_PRODUCT_LOCATOR = (
        By.CSS_SELECTOR, '[class="ProductItem_productItem__2bD0C"]'
    )

    # contact

    VIBER_LOCATOR = By.XPATH, '//span[text()="Viber"]'
    A1_PHONE_LOCATOR = (
        By.CSS_SELECTOR, '[class*="styles_textCursor__ecphd"]'
    )

    # contact drop-list

    CONTACTS_DROP_LIST_LOCATOR = By.XPATH, '(//*[text()="Еще"])[2]'
    LIFE_PHONE_LOCATOR = (
        By.XPATH, '(//li[@class="styles_communicationListItem___jHWt '
                  'styles_inactive__1IrDM"])[1]'
    )
    LANDLINE_PHONE_LOCATOR = (
        By.XPATH, '(//li[@class="styles_communicationListItem___jHWt '
                  'styles_inactive__1IrDM"])[2]'
    )
    TELEGRAM_LOCATOR = (
        By.XPATH, '(//li[@class="styles_listItem__ZxDwC styles_communication'
                  'ListItem___jHWt"])[1]'
    )
    EMAIL_LOCATOR = (
        By.XPATH,'(//li[@class="styles_listItem__ZxDwC styles_communication'
                 'ListItem___jHWt"])[2]'
    )
    ORDER_A_CALL = (
        By.XPATH, '(//li[@class="styles_listItem__ZxDwC styles_communicati'
                  'onListItem___jHWt"])[3]'
    )
    BUTTON_WRITE_TO_US_LOCATOR = (
        By.XPATH, '(//li[@class="styles_listItem__ZxDwC styles_communicati'
                  'onListItem___jHWt"])[4]'
    )
    CONTACTS_BUTTON_LOCATOR = (
        By.XPATH, '(//li[@class="styles_listItem__ZxDwC styles_communicatio'
                  'nListItem___jHWt"])[5]'
    )
    REQUEST_A_CALL_LOCATOR = By.XPATH,  '//*[text()="Заказать звонок"]'
    ASK_A_QUESTION_LOCATOR = By.XPATH,  '//*[text()="Задать вопрос"]'
    CLOSE_FEEDBACK_LOCATOR = (
        By.CSS_SELECTOR, '[class*="styles_closeModalIcon__PV5qz"]'
    )

    #

    a = '(//*[text()="Еще"])[1]'
