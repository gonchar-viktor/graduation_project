import pytest
from data.urls import BOOK_PAGE_URL
from pages.main_page import MainPage
from conftest import driver
import allure


class TestHeader:

    @allure.feature('product catalog')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks product catalog')
    def test_product_catalog_button(self, driver):
        """Checks that when you click on the "product catalog" button, the
        categories of all products are displayed."""
        with allure.step('open main page'):
            header = MainPage(driver)
            header.open_page_and_reject_cookies()
        with allure.step('click on button product catalog'):
            header.hard_click(header.PRODUCT_CATALOG_BUTTON_LOCATOR)
        with allure.step('checking element display'):
            header.assert_categories_displayed()

    @allure.feature('Logotype')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks logo')
    def test_click_on_logotype(self, driver):
        """Checks that the logo is visible on page and when clicked on it,
        the main page of the site opens."""
        header = MainPage(driver)
        header.open_page_and_reject_cookies()
        header.click_on(header.LOGOTYPE_LOCATOR)
        header.assert_actual_url_click_logotype()

    @allure.feature('city selection')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks display city for delivery')
    @pytest.mark.parametrize(
        'selection_city', ['г. Минск', 'г. Брест', 'г. Витебск'])
    def test_city_selection(self, driver, selection_city):
        """Checks that you can change the city for delivery, and it will be
        displayed on the site."""
        header = MainPage(driver)
        header.open_page_and_reject_cookies()
        header.click_on_city_selection_button()
        header.fill(header.INPUT_CITY_SELECTION_LOCATOR, selection_city)
        header.confirm_city_selection()
        header.click_on_save_button()
        header.wait_for_element_to_change(
            header.CITY_SELECTION_BUTTON_LOCATOR, selection_city)
        header.assert_text_in_element(
            header.CITY_SELECTION_BUTTON_LOCATOR, selection_city)

    @allure.feature('Catalog search')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks the page of the entered product')
    def test_catalog_search(self, driver):
        """Enters the name of the product in the input field, selects the
        product and checks that the desired page has opened."""
        header = MainPage(driver)
        header.open_page_and_reject_cookies()
        header.enter_product_text(header.request_text)
        header.click_on_product(header.CHOOSE_PRODUCT_LOCATOR)
        header.assert_actual_url(BOOK_PAGE_URL)

    @allure.feature('Header line')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks the opening of pages from the title bar')
    def test_header_line(self, driver):
        """Checks that all pages from the header line open correctly
        when opened."""
        header = MainPage(driver)
        header.open_page_and_reject_cookies()
        header.assert_all_links_lead_to_the_desired_page()

    @allure.feature('Contacts')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks in header')
    def test_header_contacts(self, driver):
        """Checks that the contacts in the header, including those in the
        drop-down list, are listed correctly, and that clicking on contact
        links opens the correct pages."""
        header = MainPage(driver)
        header.open_page_and_reject_cookies()
        header.assert_correct_visible_contact_a1()
        header.assert_viber_link_header()
        header.assert_contacts_from_the_drop_down_list()
        header.assert_link_from_the_drop_down_list()

    @allure.feature('contact center')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks contact center')
    def test_information_contact_center(self, driver):
        """Checks that the information about the work of the contact center
        is indicated on the website correctly."""
        header = MainPage(driver)
        header.open_page_and_reject_cookies()
        header.assert_text_in_element(
            header.CONTACT_CENTER_OPENING_HOURS_LOCATOR,
            header.CONTACT_CENTER_OPENING_HOURS_TEXT
        )

    @allure.feature('Payment and shipping')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story('Checks shipping and payment methods')
    def test_payment_and_shipping_methods(self, driver):
        """Verifies that all payment and shipping methods from the header,
        including those in the dropdown when clicked on, lead to the correct
        page."""
        header = MainPage(driver)
        header.open_page_and_reject_cookies()
        header.assert_payment_and_delivery_methods_open_correctly()
