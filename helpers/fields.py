from helpers.base import BasePage


class FieldsWebElement(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until = 10

    def fill(self, locator, text):
        self.driver.implicitly_wait(self.wait_until)
        element = self.wait_for_clicable(locator)
        element.clear()
        element.send_keys(text)

    def clear(self, locator):
        element = self.wait_for_visible(*locator)
        element.clear()
