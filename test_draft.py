import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from helpers.fields import FieldsWebElement
from helpers.assertions import Assertion
from conftest import *
from data.user import TEST_USER


# locator_account_button = By.CSS_SELECTOR,\
#     '[class="styles_userToolsIcon__Y2sGs"]'
# locator_authorized_account_button = By.CSS_SELECTOR, \
#     '[class="styles_userToolsToggler__c2aHe"]'
#
# locator_reject_button_cookies = By.CSS_SELECTOR, '[aria-label="Отклонить"]'
# link_main_page = 'https://www.21vek.by'
# locator_login_button = By.CSS_SELECTOR, '[data-testid="loginButton"]'
# #
# locator_input_mail = By.CSS_SELECTOR, '[id="login-email"]'
# locator_input_password = By.CSS_SELECTOR, '[id="login-password"]'
# locator_login_submit = By.CSS_SELECTOR, '[data-testid="loginSubmit"]'
# locator_user_tools_subtitle = By.CSS_SELECTOR, '[class="userToolsSubtitle"]'
# #
#
# locator_ass = By.XPATH, '//*[text()="Личные данные"]'
#
#
# class MainPage21vek(FieldsWebElement, Assertion):
#     pass


# class Test21Vek(MainPage21vek):
#     def reject_cookies(self):
#         """
#         A method for rejecting the agreement on the use of cookies on the site.
#         Performs a double click on the reject button.
#         """
#
#         self.hard_click(locator_reject_button_cookies)
#         self.hard_click(locator_reject_button_cookies)
#
#     def assert_that_the_user_has_logged_in(self):
#         """
#         A method to verify that the user has successfully logged into
#         the account.
#         """
#
#         self.hard_click(locator_authorized_account_button)
#         assert EC.visibility_of_element_located(locator_ass)


# @pytest.fixture(scope='function')
# def user_authorization(driver):
#     """
#     User authorization fixture on the site: https://www.21vek.by.
#     Steps:
#         1. Initializes an object of the Test21vek class with the driver passed
#         in the parameter.
#         2. Opens the main page of the site.
#         3. Rejects the cookie usage agreement.
#         4. Clicks on the account button.
#         5. Presses the login button.
#         6. Fills in the email input field with the value from the TEST_USER
#         variable.
#         7. Fills in the password input field with the value from the TEST_USER
#         variable.
#         8. Presses the login confirmation button.
#         9. Checks that the user has successfully logged into the account.
#     """
#
#     page = Test21Vek(driver)
#     page.driver.get(link_main_page)
#     page.reject_cookies()
#     page.hard_click(locator_account_button)
#     page.hard_click(locator_login_button)
#     page.fill(locator_input_mail, TEST_USER.get('email'))
#     page.fill(locator_input_password, TEST_USER.get('password'))
#     page.hard_click(locator_login_submit)
#     page.assert_that_the_user_has_logged_in()

#
# def test_logged_new_sessions(user_authorization, driver):
#     """
#     Precondition: the user must be logged in to the site.
#
#     The test checks the user's automatic login to the account in a new session.
#     Steps:
#         1. Opens a new tab in the browser.
#         2. Switches to a new tab.
#         3. Opens the main page of the site in a new tab.
#         4. Initializes an object of the Test21vek class with the driver passed
#         in the parameter.
#         5. Checks that the user has successfully logged into the account on a
#         new tab of the site.
#     """
#
#     driver.execute_script("window.open()")
#     handles = driver.window_handles
#     driver.switch_to.window(handles[1])
#     driver.get(link_main_page)
#     page = Test21Vek(driver)
#     page.assert_that_the_user_has_logged_in()







