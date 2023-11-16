import allure

from helpers.base import BasePage


class Cookies(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.wait_until = 10

    @allure.step('Add cookie')
    def add_cookie(self, name, value):
        self.driver.add_cookie({'name': name, 'value': value})
        self.driver.refresh()

    @allure.step('Delete cookies')
    def delete_cookies(self):
        self.driver.delete_cookies()
        self.driver.refresh()
