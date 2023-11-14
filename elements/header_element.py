import time

from data.contacts import CONTACTS
from data.urls import *
from helpers.assertions import Assertion
from helpers.fields import FieldsWebElement
from locators.header_locators import HeaderLocators
from selenium.webdriver.support import expected_conditions as EC



class HeaderElement(Assertion, FieldsWebElement, HeaderLocators):
    request_text = '9789851548299'

    def assert_categories_displayed(self):
        assert self.wait_for_visible(
            self.CATEGORIES_CONTAINER_LOCATOR).is_displayed()

    def confirm_city_selection(self):
        self.click_on(self.CONFIRM_CITY_LOCATOR)

    def click_on_save_button(self):
        self.hard_click(self.SAVE_BUTTON_LOCATOR)

    def click_on_city_selection_button(self):
        self.click_on(self.CITY_SELECTION_BUTTON_LOCATOR)

    def click_on_product(self):
        self.click_on(self.CHOOSE_PRODUCT_LOCATOR)

    def enter_product_text(self):
        self.click_on(self.CATALOG_SEARCH_LOCATOR)
        self.fill(self.CATALOG_SEARCH_LOCATOR, self.request_text)

    def assert_all_links_lead_to_the_desired_page(self):
        """The method clicks on the dictionary keys and checks that the
        required pages are opened.
        A dictionary with the values key: locator, value: page url."""

        dict_assert_links = {
            self.ALL_PROMOTIONS_LOCATOR: ALL_PROMOTIONS_PAGE_URL,
            self.MARKDOWN_LOCATOR: MARKDOWN_PAGE_URL,
            self.TIRES_LOCATOR: TIRES_PAGE_URL,
            self.REFRIGERATORS_LOCATOR: REFRIGERATORS_PAGE_URL,
            self.WASHING_MACHINES_LOCATOR: WASHING_MACHINES_PAGE_URL,
            self.BOILERS_LOCATOR: BOILERS_PAGE_URL,
            self.SMARTPHONES_LOCATOR: SMARTPHONES_PAGE_URL,
            self.LAPTOPS_LOCATOR: LAPTOPS_PAGE_URL,
            self.TELEVISIONS_LOCATOR: TELEVISIONS_PAGE_URL,
            self.VACUUM_CLEANERS_LOCATOR: VACUUM_CLEANERS_PAGE_URL,
            self.MATTRESSES_LOCATOR: MATTRESSES_PAGE_URL,
            self.SOFAS_LOCATOR: SOFAS_PAGE_URL
        }

        for key, value in dict_assert_links.items():
            self.hard_click(key)
            self.assert_actual_url(value)

    def assert_correct_visible_contact_a1(self):
        self.assert_text_in_element(
            self.A1_PHONE_LOCATOR, CONTACTS.get('a1')
        )

    def assert_viber_link_header(self):
        """Clicking on the viber icon leads to the desired page."""
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.VIBER_LOCATOR, EXPECTED_VIBER_PAGE_URL, 1
        )
        self.close_the_page_and_switch_to_page_zero()

    def assert_contacts_from_the_drop_down_list(self):
        self.click_on(self.CONTACTS_DROP_LIST_LOCATOR)
        self.assert_text_in_element(
            self.LIFE_PHONE_LOCATOR, CONTACTS.get('life')
        )
        self.assert_text_in_element(
            self.LANDLINE_PHONE_LOCATOR, CONTACTS.get('landline')
        )

    def assert_link_from_the_drop_down_list(self):
        """The method calls all the contact icons in the header drop-down
        list and checks that they open the necessary links or the necessary
        windows."""
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.TELEGRAM_LOCATOR, EXPECTED_TELEGRAM_PAGE_URL, 1
        )
        self.close_the_page_and_switch_to_page_zero()
        self.click_on(
            self.CONTACTS_DROP_LIST_LOCATOR
        )
        assert EC.element_to_be_clickable(self.EMAIL_LOCATOR)
        self.click_on(
            self.ORDER_A_CALL
        )
        assert EC.visibility_of_element_located(self.REQUEST_A_CALL_LOCATOR)
        self.click_on(
            self.CLOSE_FEEDBACK_LOCATOR
        )
        self.click_on(self.CONTACTS_DROP_LIST_LOCATOR)
        self.click_on(
            self.BUTTON_WRITE_TO_US_LOCATOR
        )
        assert EC.visibility_of_element_located(self.ASK_A_QUESTION_LOCATOR)
        self.click_on(
            self.CLOSE_FEEDBACK_LOCATOR
        )
        self.click_on(self.CONTACTS_DROP_LIST_LOCATOR)
        self.click_on(self.CONTACTS_BUTTON_LOCATOR)
        self.assert_actual_url(EXPECTED_CONTACTS_PAGE_URL)






