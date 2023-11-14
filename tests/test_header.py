import time

import pytest
from data.urls import BOOK_PAGE_URL
from pages.main_page import MainPage
from conftest import driver
from pages.laptops_page import NotebookPage


class TestHeader:
    """Class for checking the header elements:
        -
        -
        -
        -"""

    def test_product_catalog_button(self, driver):  # 18
        """Checks that when you click on the "product catalog" button, the
        categories of all products are displayed."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.hard_click(main_page.PRODUCT_CATALOG_BUTTON_LOCATOR)
        main_page.assert_categories_displayed()

    def test_logotype_on_laptops_page(self, driver):  # 19
        """Checks that the logo is visible on the "laptops" page and when
        clicked on it, the main page of the site opens."""
        main_page = NotebookPage(driver)
        main_page.open_laptops_page()
        main_page.reject_cookies()
        main_page.assert_actual_url_click_logotype()

    @pytest.mark.parametrize(
        'selection_city', ['г. Минск', 'г. Брест', 'г. Витебск']
    )
    def test_city_selection(self, driver, selection_city):  # 20
        """Checks that you can change the city for delivery, and it will be
        displayed on the site."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.click_on_city_selection_button()
        main_page.fill(main_page.INPUT_CITY_SELECTION_LOCATOR, selection_city)
        main_page.confirm_city_selection()
        main_page.click_on_save_button()
        main_page.assert_text_in_element(
            main_page.CITY_SELECTION_BUTTON_LOCATOR, selection_city
        )

    def test_catalog_search(self, driver):  # 21
        """Enters the name of the product in the input field, selects the
        product and checks that the desired page has opened."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.enter_product_text()
        main_page.click_on_product()
        main_page.assert_actual_url(BOOK_PAGE_URL)

    def test_header_line(self, driver):  # 22
        """Checks that all pages from the header line open correctly
        when opened."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_all_links_lead_to_the_desired_page()

    def test_header_contacts(self, driver):  # 23
        """Checks all contacts from header, including those in the
        drop-down list."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_correct_visible_contact_a1()
        main_page.assert_viber_link_header()
        main_page.assert_contacts_from_the_drop_down_list()
        main_page.assert_link_from_the_drop_down_list()









    #
    # def test_(self, driver):
    #     """f"""
    #     main_page = MainPage(driver)
    #     main_page.open_page_and_reject_cookies()






