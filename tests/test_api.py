import allure
import pytest
from all_api.api import Api
from all_api.data import Data


class TestApi:

    @pytest.mark.api
    @allure.feature("Test status")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title('Checking the opening status of the main page')
    def test_open_main_page(self):
        with allure.step('Get request to open main page'):
            response = Api.get_response_main_page()
        with allure.step('Checking the status'):
            Api.assert_request_status(response, 200)

    @pytest.mark.api
    @allure.feature('Test status and method')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Checks the request status and request method of the main '
                  'elements on the page')
    def test_loading_main_elements_of_the_page(self):
        with allure.step('Get request to loading main elements'):
            response = Api.get_response_main_elements()
        with allure.step('Checking the status all elements'):
            Api.assert_request_status_of_all_items(response)
        with allure.step('Checking the request method all elements'):
            Api.assert_requests_method_is_get_all_items(response)

    @pytest.mark.api
    @allure.feature('Login user')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Testing the user authorization on the site')
    def test_login_user(self):
        with allure.step('Post request to login user'):
            response = Api.post_request_authorization()
        with allure.step('Get user name'):
            name_user = Api.get_user_name(response)
        with allure.step('Checks that the username is correct.'):
            Api.assert_that_the_user_name_is_correct(name_user)
        with allure.step(
                'Checks whether the "name_user" object is of type string'):
            Api.assert_whether_the_object_is_of_type_string(name_user)

    @pytest.mark.api
    @allure.feature('Test basket')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Testing adding items to cart one by one')
    @pytest.mark.parametrize('payload_product',
                             [Data.product_data1, Data.product_data2])
    def test_add_product_to_basket(self, payload_product):
        with allure.step('Post request to add items to cart'):
            response = Api.post_request_add_item_to_cart(payload_product)
        with allure.step('Get data about the added product'):
            item = Api.get_item_from_cart(response)
        with allure.step('Get quantity of added product'):
            count_item = Api.get_count_item_from_cart(item)
        with allure.step('Checking the status'):
            Api.assert_request_status(response, 200)
        with allure.step(
                'Checks whether the "count_item" object is of type integer'):
            Api.assert_whether_the_object_is_of_type_integer(count_item)
        with allure.step('Check that the data parameter is in the response'):
            Api.assert_that_the_parameter_is_in_the_response(response, "data")

    @pytest.mark.api
    @allure.feature('Test basket')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title('Testing adding items to cart with incorrect data')
    def test_add_product_to_basket_with_incorrect_data(self):
        with allure.step(
                'Post request to add items to cart with incorrect data'):
            response = Api.post_request_add_item_to_cart({})
        with allure.step('Get text error'):
            error_text = Api.get_text_error(response)
        with allure.step(
                'Check that the error text matches the expected result'):
            Api.assert_text_error(Data.expected_text_error, error_text)
        with allure.step('Check that the errors parameter is in the response'):
            Api.assert_that_the_parameter_is_in_the_response(
                response, 'errors')
        with allure.step('Checking the status'):
            Api.assert_request_status(response, 422)
        with allure.step(
                'Checks whether the "error_text" object is of type string'):
            Api.assert_whether_the_object_is_of_type_string(error_text)
