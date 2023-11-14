import pytest as pytest
from data.user import TEST_USER
from locators.login_locators import LoginLocators
from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


@pytest.fixture(scope='function')
def user_authorization(driver):
    """User authorization fixture on the site: https://www.21vek.by.
    Steps:
        1. Initializes an object of the Test21vek class with the driver
        passed in the parameter.
        2. Opens the main page of the site.
        3. Rejects the cookie usage agreement.
        4. Clicks on the account button.
        5. Presses the login button.
        6. Fills in the email input field with the value from the
        TEST_USER variable.
        7. Fills in the password input field with the value from the
        TEST_USER variable.
        8. Presses the login confirmation button.
        9. Checks that the user has successfully logged into the account."""
    login_page = LoginPage(driver)
    login_page.log_in_to_the_login_window()
    login_page.fill(login_page.locator_input_email,
                    TEST_USER.get('email'))
    login_page.fill(login_page.locator_input_password,
                    TEST_USER.get('password'))
    login_page.hard_click(login_page.locator_login_submit)
    login_page.assert_that_the_user_has_logged_in()


class LoginPage(MainPage, LoginLocators):

    negative_text_email = 'test_user'
    negative_text_password = 'test_password'
    expected_message_email = 'Неправильный формат электронной почты'
    #
    expected_message_password = 'Неправильный пароль. \nСбросить пароль?'

    def assert_that_the_user_has_logged_in(self):
        """A method to verify that the user has successfully logged into
        the account."""
        self.hard_click(self.locator_authorized_account_button)
        assert EC.visibility_of_element_located(self.locator_personal_data)

    def log_in_to_the_login_window(self):
        self.driver.get(self.link_main_page)
        self.reject_cookies()
        self.hard_click(self.locator_account_button)
        self.hard_click(self.locator_login_button)

    def enter_incorrect_format_email(self):
        self.fill(self.locator_input_email, self.negative_text_email)
        self.fill(self.locator_input_password, TEST_USER.get('password'))

    def assert_error_message_email(self):
        self.assert_text_in_element(self.locator_error_message_email,
                                    self.expected_message_email)

    def enter_incorrect_password(self):
        self.fill(self.locator_input_email, TEST_USER.get('email'))
        self.fill(self.locator_input_password, '1111')

    def assert_error_message_password(self):
        self.assert_text_in_element(self.locator_error_message_password,
                                    self.expected_message_password)

    def assert_switching_to_the_new_user_registration_window(self):
        assert EC.visibility_of_element_located(self.locator_assert_register)
