import allure

from helpers.base import BasePage
from selenium.webdriver import Keys


class FieldsWebElement(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until = 10

    @allure.step('Fill field with text')
    def fill(self, locator, text):
        self.driver.implicitly_wait(self.wait_until)
        element = self.wait_for_clicable(locator)
        self.clear_input(element)
        element.send_keys(text)

    @allure.step('Clear field')
    def clear(self, locator):
        element = self.wait_for_clicable(locator)
        element.clear()

    @allure.step('Clear an input field by simulating button presses')
    def clear_input(self, locator):
        element = self.wait_for_clicable(locator)
        element.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
