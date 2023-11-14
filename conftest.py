import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOption
from selenium.webdriver.edge.options import Options as EdgeOption
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.service import Service as EdgeService

import allure
from allure_commons.types import AttachmentType


WAIT_UNTIL = 10


def pytest_addoption(parser):
    parser.addoption(
        '--headless',
        choices=('true', 'false'),
        help='Run browser in headless mode: "true" or "false"'
    )
    parser.addoption(
        '--browser',
        choices=("chrome", "edge"),
        help='Option to define type of browser'
    )


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


def create_chrome(headless):
    option_chrome = ChromeOption()
    if headless == 'true':
        option_chrome.add_argument('headless')
    driver_chrome = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=option_chrome
    )
    return driver_chrome


def create_edge(headless):
    option_edge = EdgeOption()
    if headless == 'true':
        option_edge.add_argument('headless')
    driver_edge = webdriver.Edge(
        service=EdgeService(EdgeChromiumDriverManager().install()),
        options=option_edge
    )
    return driver_edge



# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options as ChromeOptions
# from webdriver_manager.chrome import ChromeDriverManager
#
# # другой код...
#
#
# def create_driver_chrome(headless):
#     option_chrome = ChromeOptions()
#     if headless == 'true':
#         option_chrome.add_argument('headless')
#
#     service = Service(ChromeDriverManager().install())
#     driver_chrome = webdriver.Chrome(service=service, options=option_chrome)
#     return driver_chrome



# не находит локаторы и вообще неудобно работать


# def create_driver_firefox(headless):
#     option_firefox = FirefoxOption()
#     if headless == 'true':
#         option_firefox.add_argument('headless')
#
#     driver_firefox = webdriver.Firefox()
#
#     # driver_firefox = webdriver.Firefox(
#     #     service=FirefoxService(GeckoDriverManager().install()),
#     #     options=option_firefox
#     # )
#     return driver_firefox




###----------------
###----------------
import os
import time
from datetime import datetime

#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     Он используется для создания отчёта о прохождении теста.
#     возвращает результат в переменной outcome. Затем из результата в
#      переменную rep записываем отчёт о прохождении теста.
#     """
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # set a report attribute for each phase of a call, which can
#     # be "setup", "call", "teardown"
#
#     setattr(item, "rep_" + rep.when, rep)
#
#
# # check if a test has failed
# @pytest.fixture(scope="function", autouse=True)
# def test_failed_check(request):
#     """
#     Она используется для проверки, провалился ли тест или нет.
#     используя атрибут request.node.rep_setup проверяется, провалилась ли
#     установка теста, и если да, то выводится сообщение об ошибке. Если
#     установка прошла успешно, то проверяется результат выполнения самого
#     теста с помощью атрибута request.node.rep_call. Если он провалился, то
#     выполняется функция take_screenshot, которая создает скриншот с именем
#     теста, текущей датой и временем.
#     """
#
#     yield
#     # request.node is an "item" because we use the default
#     # "function" scope
#     if request.node.rep_setup.failed:
#         print("setting up a test failed!", request.node.nodeid)
#     elif request.node.rep_setup.passed:
#         if request.node.rep_call.failed:
#             driver = request.node.funcargs['driver']
#             take_screenshot(driver, request.node.nodeid)
#             print("executing test failed", request.node.nodeid)
#
#
# # make a screenshot with a name of the test, date and time
# def take_screenshot(driver, nodeid):
#     """
#     вызывается метод save_screenshot объекта driver, чтобы создать
#     скриншот, и метод attach объекта allure, чтобы добавить его в отчёт.
#     """
#
#     time.sleep(1)
#     file_name = f'{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace("/", "_").replace("::", "__")
#     driver.save_screenshot('failed_screenshot/' + file_name)
#     allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
#
# ###
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     """
#     который запускается перед и после каждого теста. Эта функция получает
#     параметры item (объект теста) и call.
#
#     результата выполнения теста и сохраняет его в переменной report. Затем
#     она проверяет, что результат выполнения теста был "call" (вызов функции
#     теста), и использует функцию setattr для добавления атрибута report к
#     объекту теста item.
#     """
#
#     report = (yield).get_result()
#     if report.when == "call":
#         setattr(item, "report", report)
#
#
# # @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# # def pytest_runtest_makereport(item, call):
# #     """
# #     Он используется для создания отчёта о прохождении теста.
# #     возвращает результат в переменной outcome. Затем из результата в
# #      переменную rep записываем отчёт о прохождении теста.
# #     """
# #
# #     outcome = yield
# #     rep = outcome.get_result()
# #     setattr(item, "rep_" + rep.when, rep)
#
#
#
# @pytest.fixture(scope='function', autouse=True)
# def make_failed_screenshot(request):
#     """
#     запускается перед каждым тестом с параметром request, содержащим
#     информацию о текущем тесте. Она используется для создания скриншота в
#      случае, если тест завершился ошибкой.
#
#     проверяет, что атрибут report объекта request.node существует и имеет
#     значение failed (значение True, если тест завершился с ошибкой).
#     Затем она создает путь к сохранению скриншота, используя имя теста
#     и создает папку failed_tests_data, если она не существует. Затем она
#     сохраняет скриншот, используя метод save_screenshot объекта driver,
#     который должен быть предоставлен как аргумент driver в фикстуре. И
#     наконец, она выводит путь к ошибке (URL страницы) и путь к сохраненному
#     скриншоту.
#     """
#     yield
#     if request.node.report:
#         if request.node.report.failed:
#             path = 'failed_tests_data/'
#             if not os.path.exists(path):
#                 os.makedirs(path)
#             file_path = f'{path}{request.node.name}.png'
#             driver = request.node.funcargs['driver']
#             driver.save_screenshot(file_path)
#             print('\nError path ', driver.current_url)
#             print('\nScreenshot ', file_path)