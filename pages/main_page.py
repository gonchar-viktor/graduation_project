from selenium.common import NoSuchElementException
from conftest import driver
from data.urls import DOMAIN
from elements.footer_element import FooterElement
from elements.header_element import HeaderElement
from helpers.cookies import Cookies
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
import allure


class MainPage(FooterElement, Cookies, HeaderElement, MainPageLocators):
    expected_text_title = 'Онлайн-гипермаркет 21vek.by'

    @allure.severity(allure.severity_level.BLOCKER)
    def open(self):
        with allure.step('open main page'):
            self.driver.get(DOMAIN)

    @allure.step('Reject cookies')
    def reject_cookies(self):
        """A method for rejecting the agreement on the use of cookies on the
        site. Performs a double click on the reject button."""

        self.hard_click(self.locator_reject_button_cookies)
        self.hard_click(self.locator_reject_button_cookies)

    @allure.step('Open page and reject cookies')
    def open_page_and_reject_cookies(self):
        self.open()
        self.reject_cookies()

    @allure.step('Assert banners and widgets is displayed')
    def assert_banners_and_widgets_is_displayed(self):
        list_locators = [
            self.BANNER_LOCATOR, self.SUGGESTED_MANUFACTURERS_LOCATOR,
            self.ALL_PROMOTIONS_WIDGETS_LOCATOR, self.OFFERS_WIDGETS_LOCATOR,
            self.POPULAR_WIDGETS_LOCATOR, self.REVIEWS_WIDGETS_LOCATOR
        ]

        for i in list_locators:
            self.assert_element_is_displayed(i)

    def assert_text_title(self):
        with allure.step('assert text from the title'):
            assert self.expected_text_title == self.driver.title

    @allure.step('Assert adding products to favorites')
    def assert_adding_products_to_favorites(self, range_val):
        """Checks that all products in the "all promotions" section can be
        added to favorites. Every 5 products the widget scrolls to the left."""
        for i in range(1, range_val):
            param_locator = (
                By.XPATH,
                f"(//*[contains(@class, 'ProductHome_favoritesButtonSp"
                f"ecialOffers__qX1El')])[{i}]"
            )
            if i == 6 or i == 11 or i == 15:
                self.click_on(self.SLIDE_ALL_PROMOTIONS_LOCATOR)
            try:
                element = self.wait_for_visible(param_locator)
                print(param_locator)
                assert element.is_enabled(), \
                    f"Locator {param_locator} is not clickable"
            except NoSuchElementException:
                assert False, f"Locator {param_locator} is not found"
