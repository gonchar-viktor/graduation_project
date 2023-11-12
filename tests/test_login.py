import pytest
from selenium.webdriver.support import expected_conditions as EC
from data import TEST_USER
from pages.login_page import user_authorization, LoginPage
from conftest import driver


class TestAuthorizationWindow:
    """Class for checking the user authorization window"""

    def test_user_will_be_logged_new_sessions(
            self, user_authorization, driver):  # 5
        """Precondition: the user must be logged in to the site.
        The test checks the user's automatic login to the account in a new
        session. Steps:
            1. Opens a new tab in the browser.
            2. Switches to a new tab.
            3. Opens the main page of the site in a new tab.
            4. Initializes an object of the Test21vek class with the driver
            passed in the parameter.
            5. Checks that the user has successfully logged into the account
            on a new tab of the site."""

        login_page = LoginPage(driver)
        login_page.driver.execute_script("window.open()")
        handles = login_page.driver.window_handles
        login_page.driver.switch_to.window(handles[1])
        login_page.driver.get(login_page.link_main_page)
        login_page.assert_that_the_user_has_logged_in()

    def test_valid_mail_format(self, driver):  # 6
        """Checks the valid mail format for authorization."""
        login_page = LoginPage(driver)
        login_page.log_in_to_the_login_window()
        login_page.fill(
            login_page.locator_input_email,
            login_page.negative_text_email
        )
        login_page.fill(
            login_page.locator_input_password,
            login_page.negative_text_password
        )
        login_page.hard_click(login_page.locator_login_submit)
        login_page.assert_text_in_element(
            login_page.locator_error_message_email,
            login_page.expected_message_email
        )

    def test_invalid_password(self, driver):  # 7
        """Checks the valid password for authorization."""
        login_page = LoginPage(driver)
        login_page.log_in_to_the_login_window()
        login_page.fill(login_page.locator_input_email, TEST_USER.get('email'))
        login_page.fill(login_page.locator_input_password, '1111')
        login_page.hard_click(login_page.locator_login_submit)
        login_page.assert_text_in_element(
            login_page.locator_error_message_password,
            login_page.expected_message_password)

    def test_possible_to_register_a_new_user(self, driver):  # 8
        """Checks that it is possible to register a new user by clicking the
        "Registration" button in the authorization window."""
        login_page = LoginPage(driver)
        login_page.log_in_to_the_login_window()
        login_page.hard_click(login_page.locator_button_register)
        EC.visibility_of_element_located(login_page.locator_assert_register)
