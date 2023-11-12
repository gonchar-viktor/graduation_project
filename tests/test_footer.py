import time
import pytest
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from data.user import TEST_USER
from data.urls import *
from pages.main_page import MainPage


class TestFooter:


    # загружены все элементы нижнего колонтитула


    class TestContactsElement:
        """Class for checking contacts in footer."""
        def test_contacts_in_footer_are_visible(self, driver):  # 1
            """Checks that the contacts are displayed."""
            main_page = MainPage(driver)
            main_page.open_page_and_reject_cookies()
            main_page.assert_element_is_displayed(
                main_page.CONTACTS_FOOTER_LOCATOR)

        def test_correct_display_of_numbers_in_footer(self, driver):  # 2
            """Checks that phones are displayed correctly in footer."""
            main_page = MainPage(driver)
            main_page.open_page_and_reject_cookies()
            main_page.assert_the_numbers_footer_are_displayed_correctly()

        def test_footer_links(self, driver):  # 3
            """Checks that when links viber and telegram are clicked,
            they open the correct pages."""
            main_page = MainPage(driver)
            main_page.open_page_and_reject_cookies()
            main_page.assert_footer_links_viber_and_telegram_correct()

        def test_window_feedback(self, driver):  # 4
            """Checks that it is possible to fill out and send SMS
            about feedback."""
            main_page = MainPage(driver)
            main_page.open_page_and_reject_cookies()
            main_page.hard_click(main_page.BUTTON_WRITE_TO_US_LOCATOR)
            main_page.fill_name_for_feedback()
            main_page.fill_email_for_feedback()
            main_page.fill_message_for_feedback()
            main_page.assert_confirmation_button_is_clickable()

    class TestSocialNetworksElements:
        """Class for checking social networks in footer."""

        def test_social_networks_display(self, driver):  # 9
            """Checks that the social networks are displayed."""
            main_page = MainPage(driver)
            main_page.open_page_and_reject_cookies()
            main_page.assert_element_is_displayed(
                main_page.SOCIAL_NETWORKS_LOCATOR)

        def test_click_link_social_networks(self, driver):  # 10
            """Checks every social network icon."""
            main_page = MainPage(driver)
            main_page.open_page_and_reject_cookies()
            main_page.assert_link_social_networks_correct()

        def test_text_title_columns(self, driver):  # 11
            """Checking the text from the title columns."""
            main_page = MainPage(driver)
            main_page.open_page_and_reject_cookies()
            main_page.assert_title_text()


        #
        # def test_(self, driver):
        #     """ffff"""
        #
        #     main_page = MainPage(driver)
        #     main_page.open_page_and_reject_cookies()
        #
        # def test_(self, driver):
        #     """ffff"""
        #
        #     main_page = MainPage(driver)
        #     main_page.open_page_and_reject_cookies()
        #
        # def test_(self, driver):
        #     """ffff"""
        #
        #     main_page = MainPage(driver)
        #     main_page.open_page_and_reject_cookies()



