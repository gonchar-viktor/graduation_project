from conftest import driver
from data.urls import DOMAIN
from elements.footer_element import FooterElement
from elements.header_element import HeaderElement
from helpers.cookies import Cookies
from locators.main_page_locators import MainPageLocators


class MainPage(FooterElement, Cookies, HeaderElement, MainPageLocators):

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

