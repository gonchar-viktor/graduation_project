import allure

from data.contacts import CONTACTS
from data.urls import *
from helpers.assertions import Assertion
from helpers.fields import FieldsWebElement
from locators.header_locators import HeaderLocators
from selenium.webdriver.support import expected_conditions as EC


class HeaderElement(Assertion, FieldsWebElement, HeaderLocators):
    CONTACT_CENTER_OPENING_HOURS_TEXT = 'контакт-центр\nс 8:00 до 22:00'
    request_text = 'Книга Попурри Самый богатый человек в Вавилоне / 97898' \
                   '51548299 (Клейсон Дж.)'

    @allure.step('Assert categories displayed')
    def assert_categories_displayed(self):
        assert self.wait_for_visible(
            self.CATEGORIES_CONTAINER_LOCATOR).is_displayed()

    @allure.step('Confirm city selection')
    def confirm_city_selection(self):
        self.hard_click(self.CONFIRM_CITY_LOCATOR)

    @allure.step('Click on save button')
    def click_on_save_button(self):
        self.hard_click(self.SAVE_BUTTON_LOCATOR)

    @allure.step('Click on city selection button')
    def click_on_city_selection_button(self):
        self.click_on(self.CITY_SELECTION_BUTTON_LOCATOR)

    @allure.step('enter the city in the input field')
    def enter_the_city_in_the_input_field(self, selected_city):
        self.fill(self.INPUT_CITY_SELECTION_LOCATOR, selected_city)

    @allure.step('wait until the city changes')
    def wait_until_the_city_changes(self, selected_city):
        self.wait_for_element_to_change(
            self.CITY_SELECTION_BUTTON_LOCATOR, selected_city)

    @allure.step('assert contact center text')
    def assert_contact_center_text(self):
        self.assert_text_in_element(self.CONTACT_CENTER_OPENING_HOURS_LOCATOR,
                                    self.CONTACT_CENTER_OPENING_HOURS_TEXT
                                    )

    @allure.step('Click on product')
    def click_on_product(self, product):
        self.click_on(product)

    @allure.step('Enter product text')
    def enter_product_text(self, product):
        self.click_on(self.CATALOG_SEARCH_LOCATOR)
        self.fill(self.CATALOG_SEARCH_LOCATOR, product)

    @allure.step('Assert all links lead to the desired page')
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

    @allure.step('Assert correct visible contact a1')
    def assert_correct_visible_contact_a1(self):
        self.assert_text_in_element(
            self.A1_PHONE_LOCATOR, CONTACTS.get('a1'))

    @allure.step('assert viber link header')
    def assert_viber_link_header(self):
        """Clicking on the viber icon leads to the desired page."""
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.VIBER_LOCATOR, EXPECTED_VIBER_PAGE_URL, 1
        )
        self.close_the_page_and_switch_to_page_zero()

    @allure.step('Assert contacts from the drop down list')
    def assert_contacts_from_the_drop_down_list(self):
        self.click_on(self.CONTACTS_DROP_LIST_LOCATOR)
        self.assert_text_in_element(
            self.LIFE_PHONE_LOCATOR, CONTACTS.get('life')
        )
        self.assert_text_in_element(
            self.LANDLINE_PHONE_LOCATOR, CONTACTS.get('landline')
        )

    @allure.step('Assert link from the drop down list')
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

    @allure.step('Assert payment and delivery methods open correctly')
    def assert_payment_and_delivery_methods_open_correctly(self):
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.PAYMENT_IN_INSTALLMENTS_LOCATOR,
            PAYMENT_IN_INSTALLMENTS_PAGE_URL, 0
        )
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.BONUS_PROGRAM_LOCATOR, BONUS_PROGRAM_PAGE_URL, 0
        )

        self.click_on(self.PAYMENT_AND_DELIVERY_DROP_LIST_LOCATOR)
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.PAYMENT_LOCATOR, PAYMENT_PAGE_URL, 0
        )
        self.click_on(self.PAYMENT_AND_DELIVERY_DROP_LIST_LOCATOR)
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.DELIVERY_LOCATOR, DELIVERY_PAGE_URL, 0
        )
        self.click_on(self.PAYMENT_AND_DELIVERY_DROP_LIST_LOCATOR)
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.SELF_DELIVERY_LOCATOR, SELF_DELIVERY_PAGE_URL, 0
        )

    @allure.step('Assert actual url click logotype')
    def assert_actual_url_click_logotype(self):
        self.wait_for_visible(self.LOGOTYPE_LOCATOR)
        self.click_on(self.LOGOTYPE_LOCATOR)
        self.assert_actual_url(DOMAIN)
