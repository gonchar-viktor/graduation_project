from selenium.webdriver.common.by import By


class FooterLocators:
    #   contacts element

    CONTACTS_FOOTER_LOCATOR = By.CLASS_NAME, 'Contacts_contactsBlock__zhJiB'
    A1_PHONE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="Contacts_contactsBlockItem__Q_Lbt Contacts_a1__i0HVH"]'
    )
    LIFE_PHONE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="Contacts_contactsBlockItem__Q_Lbt Contacts_life__og0AR"]'
    )
    LANDLINE_PHONE_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="Contacts_contactsBlockItem__Q_Lbt Contacts_home__N_noA"]'
    )

    #

    VIBER_FOOTER_LOCATOR = By.XPATH, '//a[text()="Viber"]'
    TELEGRAM_FOOTER_LOCATOR = By.XPATH, '//a[text()="Telegram"]'
    BUTTON_WRITE_TO_US_LOCATOR = By.XPATH, '//span[text()="Написать нам"]'

    #   Feedback window

    INPUT_NAME_LOCATOR = By.CSS_SELECTOR, 'input[label="Имя"]'
    INPUT_EMAIL_LOCATOR = (
        By.CSS_SELECTOR, 'input[label="Электронная почта или номер телефона"]'
    )
    INPUT_MESSAGE_LOCATOR = By.CSS_SELECTOR, 'textarea[label="Сообщение"]'
    CONFIRMATION_ICON_LOCATOR = (
        By.CSS_SELECTOR, '[clip-path="url(#clip0_4489_3313)"]'
    )
    text_message = 'Когда будет распродажа?'
    SEND_BUTTON_LOCATOR = By.XPATH, '//div[text()="Отправить"]'
    MESSAGE_HAS_BEEN_SENT_LOCATOR = (
        By.XPATH, '//*[text()="Сообщение отправлено"]'
    )

    #   social networks

    SOCIAL_NETWORKS_LOCATOR = (
        By.CLASS_NAME, 'styles_socialnetworksWrapper__eLNcg'
    )
    VK_LOCATOR = By.CSS_SELECTOR, '[href="https://vk.com/21vek_by"]'
    FACEBOOK_LOCATOR = (
        By.CSS_SELECTOR, '[href="https://www.facebook.com/21vek.by/"]'
    )
    INSTAGRAM_LOCATOR = (
        By.CSS_SELECTOR, '[href="https://www.instagram.com/21vek.by/"]'
    )
    YOUTUBE_LOCATOR = (
        By.CSS_SELECTOR,
        '[href="https://www.youtube.com/channel/UChNfLMJmxWcaMy1oPxxSvog"]'
    )
    DZEN_LOCATOR = (
        By.CSS_SELECTOR,
        '[href="https://zen.yandex.ru/id/5e4f94ae386b1c555647f49a"]'
    )

    #

    FIRST_TITLE_LOCATOR = By.XPATH, '(//div[@class="styles_title__OR7i8"])[1]'
    SECOND_TITLE_LOCATOR = By.XPATH, '(//div[@class="styles_title__OR7i8"])[2]'
    THIRD_TITLE_LOCATOR = By.XPATH, '(//div[@class="styles_title__OR7i8"])[3]'
    FOURTH_TITLE_LOCATOR = By.XPATH, '(//div[@class="styles_title__OR7i8"])[4]'

    #

    SUBSCRIPTION_EMAIL_LOCATOR = (
        By.CSS_SELECTOR, '[class="subscription-block-react"]'
    )
    SUBSCRIPTION_TEXT_LOCATOR = (
        By.CSS_SELECTOR, '[class="subscription-block-react__content"]'
    )
    expected_text = 'Подпишитесь и получайте больше скидок\nна весь ассорт' \
                    'имент наших товаров!'
    INPUT_SUBSCRIPTION_EMAIL_LOCATOR = (
        By.CSS_SELECTOR, '[placeholder="Введите почту"]'
    )
    BUTTON_SUBSCRIPTION_EMAIL_LOCATOR = (
        By.CSS_SELECTOR, 'button[class*="SubscriptionForm_button__PS9qv"]'
    )
    AUTHORIZATION_WINDOW_LOCATOR = (
        By.CSS_SELECTOR,
        '[class="styles_modalWrapper__5y6g7 styles_modalWrapper__aPM75"]'
    )
    AUTHORIZATION_PASSWORD_LOCATOR = By.CSS_SELECTOR, '[type="password"]'
    AUTHORIZATION_BUTTON_LOGIN_LOCATOR = (
        By.CSS_SELECTOR, '[data-testid="loginSubmit"]'
    )
    CONSENT_BUTTON_LOCATOR = By.CSS_SELECTOR, '[data-testid="agreeButton"]'

    # Information Block

    INFORMATION_BLOCK_LOCATOR = (
        By.CSS_SELECTOR, '[class="styles_legalInformationBlock__iXOVK"]'
    )

    # payment systems

    PAYMENT_SYSTEMS_LOCATOR = By.CSS_SELECTOR, '[class="styles_list__PQC5Y"]'
    WEBPAY_LOCATOR = By.CSS_SELECTOR, '[aria-label="Webpay"]'
    BELCARD_LOCATOR = By.CSS_SELECTOR, '[aria-label="Белкарт"]'
    MELTS_LOCATOR = By.CSS_SELECTOR, '[aria-label="ЕРИП"]'
    MASTERCARD_LOCATOR = By.CSS_SELECTOR, '[aria-label="Mastercard"]'
    VISA_LOCATOR = By.CSS_SELECTOR, '[aria-label="Visa"]'
