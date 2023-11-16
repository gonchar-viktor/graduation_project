import allure
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from data.contacts import CONTACTS
from data.user import TEST_USER
from data.urls import *
from helpers.assertions import Assertion
from helpers.fields import FieldsWebElement
from selenium.webdriver.support import expected_conditions as EC
from locators.footer_locators import FooterLocators


class FooterElement(Assertion, FieldsWebElement, FooterLocators):
    text_information_block = (
        'Указанные контакты также являются контактами для связи по вопросам '
        'обращения покупателей о нарушении их прав. Номер телефона работник'
        'ов местных исполнительных и распорядительных органов по месту госуд'
        'арственной регистрации ООО «Триовист», уполномоченных рассматривать'
        ' обращения покупателей: +375 17 374 01 46.\nВ торговом реестре с 23'
        ' июня 2010 г., № регистрации 156473, УНП 190806803, регистрация №19'
        '0806803, 22.02.2007, Мингорисполком.\n© 2004–2023 21vek.by, Обществ'
        'о с ограниченной ответственностью «Триовист», юр.адрес: 220020, Мин'
        'ск, пр. Победителей, 100, оф. 203 E-mail: 21@21vek.by'
    )

    @allure.step('Assert the numbers footer are displayed correctly')
    def assert_the_numbers_footer_are_displayed_correctly(self):
        """Reads the text of the specified phones and checks it with the
        expected result."""
        self.assert_text_in_element(
            self.A1_PHONE_LOCATOR, CONTACTS.get('a1')
        )
        self.assert_text_in_element(
            self.LIFE_PHONE_LOCATOR, CONTACTS.get('life')
        )
        self.assert_text_in_element(
            self.LANDLINE_PHONE_LOCATOR, CONTACTS.get('landline')
        )

    @allure.step('Assert footer links viber and telegram correct')
    def assert_footer_links_viber_and_telegram_correct(self):
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.VIBER_FOOTER_LOCATOR, EXPECTED_VIBER_PAGE_URL, 1)
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.TELEGRAM_FOOTER_LOCATOR, EXPECTED_TELEGRAM_PAGE_URL, 1)

    @allure.step('Fill name for feedback')
    def fill_name_for_feedback(self):
        self.fill(self.INPUT_NAME_LOCATOR, TEST_USER.get('name'))

    @allure.step('Fill email for feedback')
    def fill_email_for_feedback(self):
        self.fill(self.INPUT_EMAIL_LOCATOR, TEST_USER.get('email'))

    @allure.step('Fill message for feedback')
    def fill_message_for_feedback(self):
        self.fill(self.INPUT_MESSAGE_LOCATOR, self.text_message)

    @allure.step('')
    def assert_confirmation_button_is_clickable(self):
        assert EC.element_to_be_clickable(self.SEND_BUTTON_LOCATOR)

    @allure.step('Assert confirmation button is clickable')
    def assert_link_social_networks_correct(self):
        """The method clicks on each icon of the social network and checks
        that the desired page opens."""
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.VK_LOCATOR, VK_PAGE_URL, 1
        )
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.FACEBOOK_LOCATOR, FACEBOOK_PAGE_URL, 1
        )
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.INSTAGRAM_LOCATOR, INSTAGRAM_PAGE_URL, 1
        )
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.YOUTUBE_LOCATOR, YOUTUBE_PAGE_URL, 1
        )
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.DZEN_LOCATOR, DZEN_PAGE_URL, 1
        )

    @allure.step('Assert title text')
    def assert_title_text(self):
        """Compares the text from the lower titles with the expected result."""
        self.assert_text_in_element(
            self.FIRST_TITLE_LOCATOR, 'Покупателям'
        )
        self.assert_text_in_element(
            self.SECOND_TITLE_LOCATOR, 'Выгодные предложения'
        )
        self.assert_text_in_element(
            self.THIRD_TITLE_LOCATOR, 'Компания'
        )
        self.assert_text_in_element(
            self.FOURTH_TITLE_LOCATOR, 'Полезная информация'
        )

    @allure.step('Checking the clickability of locators from the title')
    def checking_the_clickability_of_locators_from_the_title(self, range_val):
        """The method checks all received locators from the title
        for clickability."""
        for i in range(1, range_val):
            param_locator = (
                By.XPATH,
                f'(//*[@class="styles_sitemapItem__Novv5"])[{i}]'
            )
            try:
                element = self.wait_for_visible(param_locator)
                print(param_locator)
                assert element.is_enabled(), \
                    f"Locator {param_locator} is not clickable"
            except NoSuchElementException:
                assert False, f"Locator {param_locator} is not found"

    @allure.step('Assert display of the email subscription element')
    def assert_display_of_the_email_subscription_element(self):
        assert self.wait_for_visible(
            self.SUBSCRIPTION_EMAIL_LOCATOR).is_displayed()

    @allure.step('Assert display of payment systems')
    def assert_display_of_payment_systems(self):
        lst = [
            self.PAYMENT_SYSTEMS_LOCATOR, self.WEBPAY_LOCATOR,
            self.BELCARD_LOCATOR, self.MELTS_LOCATOR, self.VISA_LOCATOR,
            self.MASTERCARD_LOCATOR
        ]
        for i in lst:
            try:
                element = self.wait_for_visible(i)
                print(i)
                assert element.is_enabled, f"Locator {i} is not clickable"
            except NoSuchElementException:
                assert False, f"Locator {i} is not found"
