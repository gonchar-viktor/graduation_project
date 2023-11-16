import allure
import pytest as pytest
from data.user import TEST_USER
from locators.login_locators import LoginLocators
from pages.main_page import MainPage
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver


@allure.step('User authorization')
@pytest.fixture(scope='function')
def user_authorization(driver):
    """User authorization fixture on the site"""
    with allure.step('Initializes an object of the LoginPage class'):
        login_page = LoginPage(driver)
    login_page.log_in_to_the_login_window()
    login_page.fill_email()
    login_page.fill_password()
    login_page.confirm_data()
    login_page.assert_that_the_user_has_logged_in()


class LoginPage(MainPage, LoginLocators):
    negative_text_email = 'test_user'
    negative_text_password = 'test_password'
    expected_message_email = 'Неправильный формат электронной почты'
    expected_message_password = 'Неправильный пароль. \nСбросить пароль?'

    @allure.step('Fill email')
    def fill_email(self):
        self.fill(
            self.locator_input_email, TEST_USER.get('email'))

    @allure.step('Fill password')
    def fill_password(self):
        self.fill(
            self.locator_input_password, TEST_USER.get('password'))

    @allure.step('Confirm data')
    def confirm_data(self):
        self.hard_click(self.locator_login_submit)

    @allure.step('Assert that the user has logged in')
    def assert_that_the_user_has_logged_in(self):
        """A method to verify that the user has successfully logged into
        the account."""
        self.hard_click(self.locator_authorized_account_button)
        assert EC.visibility_of_element_located(self.locator_personal_data)

    @allure.step('Log in to the login window')
    def log_in_to_the_login_window(self):
        self.driver.get(self.link_main_page)
        self.reject_cookies()
        self.hard_click(self.locator_account_button)
        self.hard_click(self.locator_login_button)

    @allure.step('Enter incorrect format email')
    def enter_incorrect_format_email(self):
        self.fill(self.locator_input_email, self.negative_text_email)
        self.fill(self.locator_input_password, TEST_USER.get('password'))

    @allure.step('Assert error message email')
    def assert_error_message_email(self):
        self.assert_text_in_element(self.locator_error_message_email,
                                    self.expected_message_email)

    @allure.step('Enter incorrect password')
    def enter_incorrect_password(self):
        self.fill(self.locator_input_email, TEST_USER.get('email'))
        self.fill(self.locator_input_password, '1111')

    @allure.step('Assert error message password')
    def assert_error_message_password(self):
        self.assert_text_in_element(self.locator_error_message_password,
                                    self.expected_message_password)

    @allure.step('Assert switching to the new user registration window')
    def assert_switching_to_the_new_user_registration_window(self):
        assert EC.visibility_of_element_located(self.locator_assert_register)
