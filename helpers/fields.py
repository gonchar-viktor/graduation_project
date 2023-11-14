from helpers.base import BasePage
from selenium.webdriver import Keys


class FieldsWebElement(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until = 10

    def fill(self, locator, text):
        self.driver.implicitly_wait(self.wait_until)
        element = self.wait_for_clicable(locator)
        self.clear_input(element)
        element.send_keys(text)

    def clear(self, locator):
        element = self.wait_for_clicable(locator)
        element.clear()

    def clear_input(self, locator):
        # field.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)

        element = self.wait_for_clicable(locator)
        element.send_keys(Keys.SHIFT + Keys.HOME + Keys.DELETE)
