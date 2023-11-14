import time

from helpers.base import BasePage


class Assertion(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until = 10

    def assert_text_in_element(self, locator, expected_result):
        element = self.wait_for_visible(locator)
        print(f'{element.text} = {expected_result}')
        assert element.text == expected_result, \
            f"Text not the same, '{element.text}'"

    def assert_value_in_element_attribute(
            self, locator, attribute, expected_result):
        element = self.wait_for_visible(locator)
        value = element.get_attribute(attribute)
        print(f'{value} == {expected_result}')
        assert value == expected_result, f"Attribute {value} not the same"

    def assert_actual_url(self, expected_url):
        actual_url = self.driver.current_url
        print(f'{actual_url} == {expected_url}')
        assert expected_url == actual_url, \
            f"Expected URL: {expected_url}, Actual URL: {actual_url}"

    def assert_clicking_on_the_link_opens_the_desired_page(
            self, locator, expected_result, number_page):
        self.click_on(locator)
        self.driver.switch_to.window(self.driver.window_handles[number_page])
        self.assert_actual_url(expected_result)

    def assert_element_is_displayed(self, locator):
        assert self.wait_for_visible(locator).is_displayed()
