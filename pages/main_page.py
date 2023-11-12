import pytest as pytest
from selenium.webdriver.common.by import By
from conftest import driver
from data.urls import DOMAIN
from elements.footer_element import FooterElement
from elements.header_element import HeaderElement
from helpers.assertions import Assertion
from helpers.fields import FieldsWebElement
from helpers.cookies import Cookies


class MainPage(FooterElement, Cookies, HeaderElement):

    locator_reject_button_cookies = By.CSS_SELECTOR, '[aria-label="Отклонить"]'
    link_main_page = 'https://www.21vek.by'
    locator_account_button = (
        By.CSS_SELECTOR, '[class="styles_userToolsIcon__Y2sGs"]')
    locator_authorized_account_button = (
        By.CSS_SELECTOR, '[class="styles_userToolsToggler__c2aHe"]')

    def open(self):
        self.driver.get(DOMAIN)

    def reject_cookies(self):
        """A method for rejecting the agreement on the use of cookies on the
        site. Performs a double click on the reject button."""
        self.hard_click(self.locator_reject_button_cookies)
        self.hard_click(self.locator_reject_button_cookies)

    def open_page_and_reject_cookies(self):
        self.open()
        self.reject_cookies()

