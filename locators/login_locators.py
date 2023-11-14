from selenium.webdriver.common.by import By


class LoginLocators:
    locator_login_button = By.CSS_SELECTOR, '[data-testid="loginButton"]'
    locator_input_email = By.CSS_SELECTOR, '[id="login-email"]'
    locator_input_password = By.CSS_SELECTOR, '[id="login-password"]'
    locator_login_submit = By.CSS_SELECTOR, '[data-testid="loginSubmit"]'
    locator_personal_data = By.XPATH, '//*[text()="Личные данные"]'

    # negative authorization

    locator_error_message_email = By.CLASS_NAME, 'ErrorMessage-module__message'
    locator_error_message_password = By.CLASS_NAME, 'styles_errorText__LEN7M'

    #

    locator_button_register = By.XPATH, '//*[text()="Регистрация"]'
    locator_assert_register = By.ID, 'register-email'
