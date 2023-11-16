from pages.login_page import LoginPage
from conftest import driver
from pages.login_page import user_authorization


class TestAuthorizationWindow:

    def test_user_will_be_logged_new_sessions(
            self, user_authorization, driver):
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

    def test_incorrect_email_format(self, driver):
        """Checks that if you enter an incorrect email format for
        authorization, it will generate an error message."""
        login_page = LoginPage(driver)
        login_page.log_in_to_the_login_window()
        login_page.enter_incorrect_format_email()
        login_page.hard_click(login_page.locator_login_submit)
        login_page.assert_error_message_email()

    def test_incorrect_password(self, driver):
        """Checks that if you enter the wrong password for authorization,
        an error message will be displayed."""
        login_page = LoginPage(driver)
        login_page.log_in_to_the_login_window()
        login_page.enter_incorrect_password()
        login_page.hard_click(login_page.locator_login_submit)
        login_page.assert_error_message_password()

    def test_possible_to_register_a_new_user(self, driver):
        """Checks that when you click on the “register” button for a new user
        in the authorization window, the new user registration form on the
        site opens."""
        login_page = LoginPage(driver)
        login_page.log_in_to_the_login_window()
        login_page.hard_click(login_page.locator_button_register)
        login_page.assert_switching_to_the_new_user_registration_window()
