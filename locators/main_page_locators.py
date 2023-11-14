from selenium.webdriver.common.by import By


class MainPageLocators:

    locator_reject_button_cookies = By.CSS_SELECTOR, '[aria-label="Отклонить"]'
    link_main_page = 'https://www.21vek.by'
    locator_account_button = (
        By.CSS_SELECTOR, '[class="styles_userToolsIcon__Y2sGs"]')
    locator_authorized_account_button = (
        By.CSS_SELECTOR, '[class="styles_userToolsToggler__c2aHe"]')