from selenium.webdriver.common.by import By
from data.user import TEST_USER
from data.urls import *
from helpers.assertions import Assertion
from helpers.fields import FieldsWebElement
from selenium.webdriver.support import expected_conditions as EC


class FooterElement(Assertion, FieldsWebElement):
    """
    f
    """

    #   contacts element

    CONTACTS_FOOTER_LOCATOR = By.CLASS_NAME, 'Contacts_contactsBlock__zhJiB'
    A1_PHONE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="Contacts_contactsBlockItem__Q_Lbt Contacts_a1__i0HVH"]')
    LIFE_PHONE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="Contacts_contactsBlockItem__Q_Lbt Contacts_life__og0AR"]')
    LANDLINE_PHONE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="Contacts_contactsBlockItem__Q_Lbt Contacts_home__N_noA"]')
    #
    EXPECTED_NUMBER_A1 = '+375 29 302 10 21'
    EXPECTED_NUMBER_LIFE = '+375 25 502 10 21'
    EXPECTED_NUMBER_LANDLINE_PHONE = '+375 17 302 10 21'
    #
    VIBER_FOOTER_LOCATOR = By.XPATH, '//a[text()="Viber"]'
    TELEGRAM_FOOTER_LOCATOR = By.XPATH, '//a[text()="Telegram"]'
    BUTTON_WRITE_TO_US_LOCATOR = By.XPATH, '//span[text()="Написать нам"]'

    #   Feedback window

    INPUT_NAME_LOCATOR = By.CSS_SELECTOR, 'input[label="Имя"]'
    INPUT_EMAIL_LOCATOR = (
        By.CSS_SELECTOR, 'input[label="Электронная почта или номер телефона"]')
    INPUT_MESSAGE_LOCATOR = By.CSS_SELECTOR, 'textarea[label="Сообщение"]'
    CONFIRMATION_ICON_LOCATOR = (
        By.CSS_SELECTOR, '[clip-path="url(#clip0_4489_3313)"]')
    text_message = 'Когда будет распродажа?'
    SEND_BUTTON_LOCATOR = By.XPATH, '//div[text()="Отправить"]'
    MESSAGE_HAS_BEEN_SENT_LOCATOR = (
        By.XPATH, '//*[text()="Сообщение отправлено"]')

    #   social networks

    SOCIAL_NETWORKS_LOCATOR = (
        By.CLASS_NAME, 'styles_socialnetworksWrapper__eLNcg')
    VK_LOCATOR = By.CSS_SELECTOR, '[href="https://vk.com/21vek_by"]'
    FACEBOOK_LOCATOR = (
        By.CSS_SELECTOR, '[href="https://www.facebook.com/21vek.by/"]')
    INSTAGRAM_LOCATOR = (
        By.CSS_SELECTOR, '[href="https://www.instagram.com/21vek.by/"]')
    YOUTUBE_LOCATOR = (
        By.CSS_SELECTOR,
        '[href="https://www.youtube.com/channel/UChNfLMJmxWcaMy1oPxxSvog"]')
    DZEN_LOCATOR = (
        By.CSS_SELECTOR,
        '[href="https://zen.yandex.ru/id/5e4f94ae386b1c555647f49a"]')

    #

    FIRST_TITLE_LOCATOR = By.XPATH, '(//div[@class="styles_title__OR7i8"])[1]'
    SECOND_TITLE_LOCATOR = By.XPATH, '(//div[@class="styles_title__OR7i8"])[2]'
    THIRD_TITLE_LOCATOR = By.XPATH, '(//div[@class="styles_title__OR7i8"])[3]'
    FOURTH_TITLE_LOCATOR = By.XPATH, '(//div[@class="styles_title__OR7i8"])[4]'



    #   functions and asserts

    def assert_the_numbers_footer_are_displayed_correctly(self):
        """Reads the text of the specified phones and checks it with the
        expected result."""
        self.assert_text_in_element(
            self.A1_PHONE_LOCATOR, self.EXPECTED_NUMBER_A1)
        self.assert_text_in_element(
            self.LIFE_PHONE_LOCATOR, self.EXPECTED_NUMBER_LIFE)
        self.assert_text_in_element(
            self.LANDLINE_PHONE_LOCATOR, self.EXPECTED_NUMBER_LANDLINE_PHONE)

    def assert_footer_links_viber_and_telegram_correct(self):
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.VIBER_FOOTER_LOCATOR, EXPECTED_VIBER_PAGE_URL, 1)
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.TELEGRAM_FOOTER_LOCATOR, EXPECTED_TELEGRAM_PAGE_URL, 1)

    def fill_name_for_feedback(self):
        self.fill(self.INPUT_NAME_LOCATOR, TEST_USER.get('name'))

    def fill_email_for_feedback(self):
        self.fill(self.INPUT_EMAIL_LOCATOR, TEST_USER.get('email'))

    def fill_message_for_feedback(self):
        self.fill(self.INPUT_MESSAGE_LOCATOR, self.text_message)

    def assert_confirmation_button_is_clickable(self):
        assert EC.element_to_be_clickable(self.SEND_BUTTON_LOCATOR)

    def close_the_page_and_switch_to_page_zero(self):
        """Closes the current page and goes to the start page."""
        self.driver.close()
        self.switch_to_page_zero()
        
    def assert_link_social_networks_correct(self):
        """The method clicks on each icon of the social network and checks
        that the desired page opens."""
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.VK_LOCATOR, VK_PAGE_URL, 1)
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.FACEBOOK_LOCATOR, FACEBOOK_PAGE_URL, 1)
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.INSTAGRAM_LOCATOR, INSTAGRAM_PAGE_URL, 1)
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.YOUTUBE_LOCATOR, YOUTUBE_PAGE_URL, 1)
        self.close_the_page_and_switch_to_page_zero()
        self.assert_clicking_on_the_link_opens_the_desired_page(
            self.DZEN_LOCATOR, DZEN_PAGE_URL, 1)

    def assert_title_text(self):
        """Compares the text from the lower titles with the expected result."""
        self.assert_text_in_element(
            self.FIRST_TITLE_LOCATOR, 'Покупателям')
        self.assert_text_in_element(
            self.SECOND_TITLE_LOCATOR, 'Выгодные предложения')
        self.assert_text_in_element(
            self.THIRD_TITLE_LOCATOR, 'Компания')
        self.assert_text_in_element(
            self.FOURTH_TITLE_LOCATOR, 'Полезная информация')



# @pytest.mark.parametrize('language', ["ru", "en"])
# def test_1(language):
#     print(language)
