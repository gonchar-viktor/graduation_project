from selenium.webdriver.common.by import By
from data.urls import *
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage


class NotebookPage(MainPage):

    LOGOTYPE_LOCATOR = By.CSS_SELECTOR, '[class="logotype"]'

    def open_laptops_page(self):
        self.driver.get(LAPTOPS_PAGE_URL)

    def assert_actual_url_click_logotype(self):
        self.wait_for_visible(self.LOGOTYPE_LOCATOR)
        self.click_on(self.LOGOTYPE_LOCATOR)
        self.assert_actual_url(DOMAIN)
