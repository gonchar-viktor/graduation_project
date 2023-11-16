import allure

from pages.main_page import MainPage
from conftest import driver


class TestMainPage:

    @allure.feature('Main page')
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('Check load main page ')
    def test_main_page_load(self, driver):
        """Checks that the main page of the site has loaded."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_text_title()

    @allure.feature('Banners and widgets')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('Check display all banners and widgets')
    def test_main_page_banners_and_widgets(self, driver):
        """Checks that all banners and widgets on the main page have loaded
        and are displayed."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_banners_and_widgets_is_displayed()

    @allure.feature('Favorites')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check adding to favorites all items from "all promotions"')
    def test_all_products_added_to_favorites(self, driver):
        """Checks that all products in the "all promotions" section can be
        added to favorites."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_adding_products_to_favorites(19)
