import allure

from data.user import TEST_USER
from data.urls import DOMAIN
from pages.main_page import MainPage
from conftest import driver


class TestFooter:

    @allure.feature('Contacts')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks that the contacts are displayed.')
    def test_contacts_in_footer_are_visible(self, driver):
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_element_is_displayed(footer.CONTACTS_FOOTER_LOCATOR)

    @allure.feature('Contacts')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks that phones are displayed correctly')
    def test_correct_display_of_numbers_in_footer(self, driver):
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_the_numbers_footer_are_displayed_correctly()

    @allure.feature('Contacts')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check open viber and telegram page')
    def test_footer_links(self, driver):
        """Checks that when links viber and telegram are clicked,
        they open the correct pages."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_footer_links_viber_and_telegram_correct()

    @allure.feature('Contact')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check open feedback window')
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

    @allure.feature('Social networks')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks that the social networks are displayed')
    def test_social_networks_display(self, driver):
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_element_is_displayed(footer.SOCIAL_NETWORKS_LOCATOR)

    @allure.feature('Social networks')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check open links to social networks')
    def test_click_link_social_networks(self, driver):
        """Checks that each social network icon, when clicked, opens the
        correct page."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_link_social_networks_correct()

    @allure.feature('Tittle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checking the text from the title columns')
    def test_text_title_columns(self, driver):
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_title_text()

    @allure.feature('Tittle')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check that all links from the title open')
    def test_title_links(self, driver):
        """Checking the clickability of all title links from the footer."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.checking_the_clickability_of_locators_from_the_title()

    @allure.feature('Email subscription')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks the display of the email subscription element')
    def test_email_subscription_element(self, driver):
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_display_of_the_email_subscription_element()

    @allure.feature('Email subscription')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check text in email subscription')
    def test_text_in_the_email_subscription_element(self, driver):
        """Checks whether the text in the email subscription element is
        displayed correctly."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_text_in_element(
            footer.SUBSCRIPTION_TEXT_LOCATOR, footer.expected_text)

    @allure.feature('Email subscription')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Check your subscription by email')
    def test_email_newsletter_subscriptions(self, driver):
        """Checks that you can subscribe to the newsletter by email by
        entering it in the input field located in footer."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.fill_email()
        footer.hard_click(footer.BUTTON_SUBSCRIPTION_EMAIL_LOCATOR)
        footer.assert_element_is_displayed(footer.AUTHORIZATION_WINDOW_LOCATOR)
        footer.fill_password()
        footer.click_on_button_login()
        footer.submit_consent_to_the_processing_of_personal_data()
        footer.assert_actual_url(DOMAIN)

    @allure.feature('Information_block')
    @allure.severity(allure.severity_level.TRIVIAL)
    @allure.story('Checks text in information block')
    def test_text_information_block(self, driver):
        """Checks that the information block is visible on the user's
        page, as well as that the text in it is displayed correctly."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_element_is_displayed(footer.INFORMATION_BLOCK_LOCATOR)
        footer.assert_text_in_element(
            footer.INFORMATION_BLOCK_LOCATOR, footer.text_information_block)

    @allure.feature('Payment systems')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story('Checks display payment systems')
    def test_payment_systems(self, driver):
        """Checking the display of payment systems on the page."""
        footer = MainPage(driver)
        footer.open_page_and_reject_cookies()
        footer.assert_display_of_payment_systems()
