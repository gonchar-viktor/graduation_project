from selenium.webdriver.common.by import By


class BasketLocator:

    ADD_TO_CART_BUTTON_LOCATOR = (
        By.CSS_SELECTOR, '[class*="cr-buybtn__in j-ga_track"]'
    )
    BASKET_LOCATOR = By.CSS_SELECTOR, '.headerCartBox'
    NUMBER_OF_ITEM_CART_LOCATOR = (
        By.CSS_SELECTOR, '.BasketTabsScreen_counter___R5Jp'
    )
    CHOOSE_PRODUCT_LOCATOR2 = (
        By.CSS_SELECTOR,
        '[href="/mouses/deathadderessentialrz0103850200r3m1_razer.html"]'
    )
    PRODUCT_IN_THE_CART_LOCATOR = By.CSS_SELECTOR, '.BasketItem_title__MzCQ9'

    #

    CATALOG_SEARCH_LOCATOR = By.ID, 'catalogSearch'
    CHOOSE_PRODUCT_LOCATOR = (
        By.CSS_SELECTOR, '[href="/nonfiction_books/popuri_01309.html"]'
    )

    DELETE_BUTTON_LOCATOR = By.XPATH, '//*[text()="Удалить"]'
    EMPTY_BASKET_LOCATOR = By.CSS_SELECTOR, '.EmptyBasket_text__3fMyR'
    CONFIRM_DELETE_LOCATOR = By.XPATH, '//div[text()="Удалить"]'

    #
    ADD_TO_FAVORITES_BUTTON_LOCATOR = (
        By.CSS_SELECTOR, '[aria-label="Избранное"]'
    )
    FEATURED_PRODUCT_BUTTON_LOCATOR = (
        By.XPATH, '//*[text()="Избранные товары"]'
    )
    FEATURED_PRODUCT_LOCATOR = By.CSS_SELECTOR, '.OldProductCard_card__fAG10'
