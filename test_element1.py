import time

import pytest


from elements import FooterElement
from helpers.base_gui_test import BaseGUITest
from pages.element_page import ElementPage


class TestElement(BaseGUITest):

    def test_select(self):
        self.driver.get('https://demo.guru99.com/test/newtours/reservation.php')

        element_page = ElementPage(self.driver)
        element_page.set_display_none('//*[@id="gdpr-consent-notice"]')
        element_page.select_port(element_page.select_locator, 'New York')

        self.driver.save_screenshot('select.png')

    def test_promt_alert(self):
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')

        element_page = ElementPage(self.driver)
        element_page.click_on(element_page.button_prompt_alert)
        time.sleep(2)
        element_page.prompt_alert()
        time.sleep(2)


    def test_window(self):
        self.driver.get('https://the-internet.herokuapp.com/javascript_alerts')

        element_page = ElementPage(self.driver)
        element_page.open_new_window()
        time.sleep(10)

    def test_iframe(self):
        self.driver.get('http://the-internet.herokuapp.com/iframe')

        element_page = ElementPage(self.driver)
        element_page.switch_to_iframe()

        element_page.assert_text_in_element(element_page.text_locator, 'Your content goes here.')
        self.driver.save_screenshot('select.png')

    def test_upload_file(self):
        file_path = '/Users/elenayanushevskaya/Desktop/Python Automation Engineer/HW22.txt'
        self.driver.get('http://the-internet.herokuapp.com/upload')

        element_page = ElementPage(self.driver)

        element_page.fill(element_page.file_locator, file_path)
        self.driver.save_screenshot('select1.png')

    def test_download_file1(self):
        self.driver.get('http://the-internet.herokuapp.com/download')

        element_page = ElementPage(self.driver)

        element_page.click_on('//*[@href="download/upload_file.xlsx"]')

