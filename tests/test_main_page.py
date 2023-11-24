import allure
from pages.main_page import MainPage
from conftest import driver


class TestMainPage:

    @allure.feature('Main page')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Checks that the main page of the site has loaded')
    def test_main_page_load(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_text_title()

    @allure.feature('Banners and widgets')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('Checks display all banners and widgets in main page')
    def test_main_page_banners_and_widgets(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_banners_and_widgets_is_displayed()

    @allure.feature('All promotions')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check "all promotions" section')
    def test_add_products_from_the_all_promotions_in_cart(self, driver):
        """Checks that all products from the "all promotions" section can be
        added to the cart."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_adding_product_in_cart_from_the_all_promotions()

    @allure.feature('Popular')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check "popular" section')
    def test_add_products_from_the_popular_in_cart(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.double_click_the_show_more_button()
        main_page.assert_adding_product_in_cart_from_the_popular()

    @allure.feature('Offers pages')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check open offers pages correct')
    def test_offers_pages_open(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_offers_open_correctly()

    @allure.feature('Reviews')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check click reviews')
    def test_clickability_reviews(self, driver):
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_reviews_are_clickable()
