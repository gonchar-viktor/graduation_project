from data.user import TEST_USER
from data.urls import DOMAIN
from pages.main_page import MainPage
from conftest import driver


class TestFooter:

    def test_contacts_in_footer_are_visible(self, driver):
        """Checks that the contacts are displayed."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_element_is_displayed(
            footer.CONTACTS_FOOTER_LOCATOR)

    def test_correct_display_of_numbers_in_footer(self, driver):
        """Checks that phones are displayed correctly in footer."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_the_numbers_footer_are_displayed_correctly()

    def test_footer_links(self, driver):
        """Checks that when links viber and telegram are clicked,
        they open the correct pages."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_footer_links_viber_and_telegram_correct()

    def test_window_feedback(self, driver):
        """Checks that it is possible to fill out and send SMS
        about feedback."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.hard_click(footer.BUTTON_WRITE_TO_US_LOCATOR)
        footer.fill_name_for_feedback()
        footer.fill_email_for_feedback()
        footer.fill_message_for_feedback()
        footer.assert_confirmation_button_is_clickable()

    def test_social_networks_display(self, driver):
        """Checks that the social networks are displayed."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_element_is_displayed(
            footer.SOCIAL_NETWORKS_LOCATOR)

    def test_click_link_social_networks(self, driver):
        """Checks every social network icon."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_link_social_networks_correct()

    def test_text_title_columns(self, driver):
        """Checking the text from the title columns."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_title_text()

    def test_title_links(self, driver):
        """Checking the clickability of all title links from the header."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.checking_the_clickability_of_locators_from_the_title(43)

    def test_email_subscription_element(self, driver):
        """Checks the display of the email subscription element."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_display_of_the_email_subscription_element()

    def test_text_in_the_email_subscription_element(self, driver):
        """Checks whether the text in the email subscription element is
        displayed correctly."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_text_in_element(
            footer.SUBSCRIPTION_TEXT_LOCATOR, footer.expected_text)

    def test_email_newsletter_subscriptions(self, driver):
        """Checks that you can subscribe to the newsletter by email by
        entering it in the input field located in footer."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.fill(
            footer.INPUT_SUBSCRIPTION_EMAIL_LOCATOR,
            TEST_USER.get('email')
        )
        footer.hard_click(footer.BUTTON_SUBSCRIPTION_EMAIL_LOCATOR)
        footer.assert_element_is_displayed(
            footer.AUTHORIZATION_WINDOW_LOCATOR)
        footer.fill(
            footer.AUTHORIZATION_PASSWORD_LOCATOR,
            TEST_USER.get('password')
        )
        footer.hard_click(footer.AUTHORIZATION_BUTTON_LOGIN_LOCATOR)
        footer.hard_click(footer.CONSENT_BUTTON_LOCATOR)
        footer.assert_actual_url(DOMAIN)

    def test_text_information_block(self, driver):
        """Checks that the information block is visible on the user's
        page, as well as that the text in it is displayed correctly."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_element_is_displayed(
            footer.INFORMATION_BLOCK_LOCATOR
        )
        footer.assert_text_in_element(
            footer.INFORMATION_BLOCK_LOCATOR,
            footer.text_information_block
        )

    def test_payment_systems(self, driver):
        """Checking the display of payment systems on the page."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_display_of_payment_systems()
