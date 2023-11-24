from selenium.common import NoSuchElementException
from conftest import driver
from data.urls import *
from elements.footer_element import FooterElement
from elements.header_element import HeaderElement
from helpers.cookies import Cookies
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.common.by import By
import allure


class MainPage(FooterElement, Cookies, HeaderElement, MainPageLocators):
    expected_text_title = 'Онлайн-гипермаркет 21vek.by'

    @allure.severity(allure.severity_level.BLOCKER)
    @allure.story('open main page')
    def open(self):
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

    @allure.step('Assert adding product in cart from the all '
                 'promotions section')
    def assert_adding_product_in_cart_from_the_all_promotions(self):
        for i in range(1, 21):
            param_locator = (
                By.XPATH,
                f'(//*[contains(@class, "Button-module__pink-primary")])[{i}]'
            )
            if i == 6 or i == 11 or i == 16:
                self.click_on(self.SLIDE_ALL_PROMOTIONS_LOCATOR)
            try:
                element = self.wait_for_clicable(param_locator)
                print(param_locator)
                assert element.is_enabled()
            except NoSuchElementException:
                assert False, f"Locator {param_locator} is not found"

    @allure.step('Double click the show more button')
    def double_click_the_show_more_button(self):
        self.click_on(self.SHOW_MORE_BUTTON_LOCATOR)
        self.click_on(self.SHOW_MORE_BUTTON_LOCATOR)

    @allure.step('Assert adding product in cart from the popular section')
    def assert_adding_product_in_cart_from_the_popular(self):
        for i in range(21, 51):
            param_locator = (
                By.XPATH,
                f'(//*[contains(@class, "Button-module__pink-primary")])[{i}]'
            )
            try:
                element = self.wait_for_clicable(param_locator)
                print(param_locator)
                assert element.is_enabled()
            except NoSuchElementException:
                assert False, f"Locator {param_locator} is not found"

    @allure.story('Clicks on links and checks that the right pages '
                  'are opening')
    def assert_offers_open_correctly(self):
        for i in range(1, 6):
            param_locator = (
                By.XPATH,
                f'(//*[contains(@class, "CompetitiveOffers_listItem__jmxgx"'
                f')])[{i}]'
            )
            match i:
                case 1:
                    self.click_on(param_locator)
                    self.assert_actual_url(SELF_DELIVERY_PAGE_URL)
                    self.open()
                case 2:
                    self.click_on(param_locator)
                    self.assert_actual_url(DELIVERY_PAGE_URL)
                    self.open()
                case 3:
                    self.click_on(param_locator)
                    self.assert_actual_url(PAYMENT_IN_INSTALLMENTS_PAGE_URL)
                    self.open()
                case 4:
                    self.click_on(param_locator)
                    self.assert_actual_url(BONUS_PROGRAM_PAGE_URL)
                    self.open()
                case 5:
                    self.click_on(param_locator)
                    self.assert_actual_url(GIFT_CERTIFICATES_PAGE_URL)

    def assert_reviews_are_clickable(self):
        for i in range(1, 11):
            param_locator = (
                By.XPATH,
                f'(//*[contains(@class, "ReviewsHome_card__RJ_1n")])[{i}]'
            )
            if i == 6:
                self.click_on(self.SLIDE_ALL_PROMOTIONS_LOCATOR2)
            try:
                element = self.wait_for_clicable(param_locator)
                print(param_locator)
                assert element.is_enabled()
            except NoSuchElementException:
                assert False, f"Locator {param_locator} is not found"
