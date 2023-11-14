from data.user import TEST_USER
from data.urls import DOMAIN
from pages.main_page import MainPage
from conftest import driver


class TestFooter:
    """Class for checking the footer elements:
        -contacts
        -social networks
        -title columns
        -email subscription
        -information block
        -payment systems"""

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

    #

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

    #

    def test_text_title_columns(self, driver):  # 11
        """Checking the text from the title columns."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_title_text()

    def test_title_links(self, driver):  # 12
        """Checking the clickability of all title links from the header."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.checking_the_clickability_of_locators_from_the_title(43)

    #

    def test_email_subscription_element(self, driver):  # 13
        """Checks the display of the email subscription element."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_display_of_the_email_subscription_element()

    def test_text_in_the_email_subscription_element(self, driver):  # 14
        """Checks whether the text in the email subscription element is
        displayed correctly."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_text_in_element(
            main_page.SUBSCRIPTION_TEXT_LOCATOR, main_page.expected_text)

    def test_email_newsletter_subscriptions(self, driver):  # 15
        """Checks that you can subscribe to the newsletter by email by
        entering it in the input field located in footer."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.fill(
            main_page.INPUT_SUBSCRIPTION_EMAIL_LOCATOR,
            TEST_USER.get('email')
        )
        main_page.hard_click(main_page.BUTTON_SUBSCRIPTION_EMAIL_LOCATOR)
        main_page.assert_element_is_displayed(
            main_page.AUTHORIZATION_WINDOW_LOCATOR)
        main_page.fill(
            main_page.AUTHORIZATION_PASSWORD_LOCATOR,
            TEST_USER.get('password')
        )
        main_page.hard_click(main_page.AUTHORIZATION_BUTTON_LOGIN_LOCATOR)
        main_page.hard_click(main_page.CONSENT_BUTTON_LOCATOR)
        main_page.assert_actual_url(DOMAIN)

    #

    def test_text_information_block(self, driver):  # 16
        """Checks that the information block is visible on the user's
        page, as well as that the text in it is displayed correctly."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_element_is_displayed(
            main_page.INFORMATION_BLOCK_LOCATOR
        )
        main_page.assert_text_in_element(
            main_page.INFORMATION_BLOCK_LOCATOR,
            main_page.text_information_block
        )

    #

    def test_payment_systems(self, driver):  # 17
        """Checking the display of payment systems on the page."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        main_page.assert_display_of_payment_systems()
