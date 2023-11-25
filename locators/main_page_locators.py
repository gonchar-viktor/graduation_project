from selenium.webdriver.common.by import By


class MainPageLocators:
    locator_reject_button_cookies = (
        By.CSS_SELECTOR, '[aria-label="Отклонить"]'
    )
    link_main_page = 'https://www.21vek.by'
    locator_account_button = (
        By.CSS_SELECTOR, '[class="styles_userToolsIcon__Y2sGs"]'
    )
    locator_authorized_account_button = (
        By.CSS_SELECTOR, '[class="styles_userToolsToggler__c2aHe"]'
    )

    # basic elements

    BANNER_LOCATOR = (
        By.CSS_SELECTOR, '.Carousel_swiperContainer__uZrl1'
    )
    SUGGESTED_MANUFACTURERS_LOCATOR = (
        By.CSS_SELECTOR, '.Banners_sideBannersContainer__Eofol'
    )
    ALL_PROMOTIONS_WIDGETS_LOCATOR = (
        By.CSS_SELECTOR, '[class*="SpecialOffersList_entityContent__bvcIv"]'
    )
    OFFERS_WIDGETS_LOCATOR = (
        By.XPATH, '//*[@id="content"]/div[8]/section/div'
    )
    POPULAR_WIDGETS_LOCATOR = (
        By.CSS_SELECTOR,
        'section>div[class*="PopularsList_entitylistContent__xPTiJ"]'
    )
    REVIEWS_WIDGETS_LOCATOR = (
        By.XPATH, '//*[@id="content"]/div[13]/section/div/div/div'
    )

    SLIDE_ALL_PROMOTIONS_LOCATOR = (
        By.XPATH, "(//*[contains(@class, 'SlidesPerView_right__Udl1V ')])[1]"
    )

    #

    SHOW_MORE_BUTTON_LOCATOR = (
        By.CSS_SELECTOR, '[class*="Button-module__blue-secondary"]'
    )

    #

    SLIDE_ALL_PROMOTIONS_LOCATOR2 = (
        By.XPATH, "(//*[contains(@class, 'SlidesPerView_right__Udl1V ')])[2]"
    )
