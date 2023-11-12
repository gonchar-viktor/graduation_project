from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from conftest import driver


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_until = 10

    # expectations
    def wait_for_clicable(self, locator):
        """Waiting until the element becomes clickable otherwise an error will
        be caused."""
        try:
            return WebDriverWait(self.driver, self.wait_until).until(
                EC.element_to_be_clickable(locator))
        except WebDriverException:
            assert False, f"Element {locator} not clicable"

    def wait_for_visible(self, locator):
        """Waiting until the element becomes visible, otherwise an error will
        be caused."""
        try:
            return WebDriverWait(self.driver, self.wait_until).until(
                EC.visibility_of_element_located(locator))
        except WebDriverException:
            assert False, f"Element {locator} not visible"

    # clicks

    def hard_click(self, locator):
        element = self.wait_for_clicable(locator)
        self.driver.execute_script("arguments[0].click();", element)

    def click_on(self, locator):
        element = self.wait_for_clicable(locator)
        element.click()
    #

    def get_current_url(self):
        return self.driver.current_url

    def get_attribute_func(self, locator, text):
        return self.driver.find_element(*locator).get_attribute(text)

    # scrolls
    def scroll_the_page_to_the_element(self, val):
        """The function scrolls the page to the specified element.
        :param val: The element to which the page scrolls."""
        element_interactions = self.wait_for_clicable(val)
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", element_interactions)

    def scroll_down_to_end(self):
        """The function scrolls the page to the end"""
        scroll_height = 1000
        while True:
            self.driver.execute_script(
                f"window.scrollTo(0, {scroll_height});")
            scroll_height += 1000

            if scroll_height >= self.driver.execute_script(
                    "return document.body.scrollHeight;"):
                break
    #

    def open_new_window(self):
        self.driver.execute_script("window.open()")
        handles = self.driver.window_handles
        self.driver.switch_to.window(handles[1])
        self.driver.close()

    def select_by_value(self, select, value):
        element = self.wait_for_visible(select)
        select = Select(element)
        select.select_by_value(value)

    def switch_to_iframe(self):
        self.driver.switch_to.frame(self.wait_for_visible('//iframe'))

    def set_display_none(self, locator):
        element = self.wait_for_visible(locator)
        self.driver.execute_script('arguments[0].setAttribute("display",'
                                   ' arguments[1])', element, 'none')

    def prompt_alert(self):
        alert = self.driver.switch_to.alert
        print(alert.text)
        alert.send_keys("Answer")
        alert.accept()

    #
    def switch_to_page_zero(self):
        self.driver.switch_to.window(self.driver.window_handles[0])
