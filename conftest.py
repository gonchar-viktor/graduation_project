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
    driver_browser = None
    headless = request.config.getoption('--headless', default='false')
    browser = request.config.getoption('--browser', default='chrome')

    if browser == 'chrome':
        driver_browser = create_chrome(headless)
    elif browser == 'edge':
        driver_browser = create_edge(headless)

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

###

# import logging
# import logging.config
# import allure
# import pytest
# # from httpbin_test.config import dict_log_config, file_name_for_logging
# from httpbin import HttpBin
#
#
# file_name_for_logging = "tests.log"
# dict_log_config = {
#     "version": 1,
#     "handlers": {
#         "fileHandler": {
#             "class": "logging.FileHandler",
#             "formatter": "myFormatter",
#             "filename": file_name_for_logging
#         }
#     },
#     "loggers": {
#         "test": {
#             "handlers": ["fileHandler"],
#             "level": "INFO",
#         }
#     },
#     "formatters": {
#         "myFormatter": {
#             "format": "%(asctime)s - %(levelname)s - %(message)s"
#         }
#     }
# }
#
#
# @pytest.fixture(scope="function")
# @pytest.mark.asyncio
# async def prepare_for_test():
#     """
#     Fixture for create and close user session.
#     """
#     httpbin = HttpBin()
#     yield httpbin
#     await httpbin.close()
#
#
# @pytest.fixture(scope="function")
# def logger():
#     """
#     Fixture for logging.
#     """
#     logging.config.dictConfig(dict_log_config)
#     logger = logging.getLogger("test")
#     allure.attach.file(file_name_for_logging, 'LOG')
#     return logger
