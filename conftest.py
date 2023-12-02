import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.edge.options import Options as EdgeOption
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

import allure

WAIT_UNTIL = 10


def pytest_addoption(parser):
    parser.addoption(
        '--headless',
        choices=('true', 'false'),
        default='false',
        help='Run browser in headless mode: "true" or "false"'
    )
    parser.addoption(
        '--browser',
        choices=("chrome", "edge"),
        default='chrome',
        help='Option to define type of browser'
    )


@allure.feature('browser selection and options')
@pytest.fixture(autouse=True)
def driver(request):
    headless = request.config.getoption('--headless', default='false')
    browser = request.config.getoption('--browser', default='chrome')

    if browser == 'chrome':
        driver_browser = create_chrome(headless)
    elif browser == 'edge':
        driver_browser = create_edge(headless)
    else:
        raise ValueError(f"Invalid browser option: {browser}")

    driver_browser.implicitly_wait(WAIT_UNTIL)
    driver_browser.maximize_window()
    yield driver_browser
    driver_browser.close()
    driver_browser.quit()


@allure.story('creating a chrome browser')
def create_chrome(headless):
    option_chrome = ChromeOption()
    if headless == 'true':
        option_chrome.add_argument('headless')
    driver_chrome = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=option_chrome
    )
    return driver_chrome


@allure.story('creating a edge browser')
def create_edge(headless):
    option_edge = EdgeOption()
    if headless == 'true':
        option_edge.add_argument('headless')
    driver_edge = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=option_edge
    )
    return driver_edge
