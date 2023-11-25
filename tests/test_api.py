import allure
import pytest
import json
from all_api.models import AuthorizationUser
from data import DOMAIN
from all_api.api import Api
from all_api.data import Data


class TestApi:

    @allure.feature("Main page")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('Testing status and output of the request time')
    def test_main_page(self):
        response = Api(DOMAIN).get_requests()
        print(response.headers['date'])
        try:
            assert response.status == 200
            assert 'date' in response.headers
        except json.JSONDecodeError:
            assert False, f"Status code incorrect -- {response.status}!= 200"

    @allure.feature('Main elements of the page')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('Testing status and request method')
    def test_main_elements_of_the_page(self):
        """Checks the request status and request method of the main elements
        on the page"""
        headers = Data.headers
        for url in Data.urls_main_elements_of_the_page:
            response = Api(url).get_requests(headers)
            try:
                assert response.status == 200
                assert '<PreparedRequest [GET]>' == f'{response.request}'
            except json.JSONDecodeError:
                assert False, f"The status code or request method is not " \
                              f"correct"

    @allure.feature('Login user')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('Testing login user and his name')
    def test_login(self):
        """Checks the user's authorization on the site, and checks that the
        username is correct"""
        data = AuthorizationUser.user_data()
        headers = Data.headers_user_login
        response = Api(DOMAIN).authorization_user(data, headers)
        name_user = response.response['user']['name']
        print(f"\nUsername is  = '{name_user}'")
        try:
            assert name_user == 'test user name'
            assert isinstance(name_user, str)
        except json.JSONDecodeError:
            assert False, f"User is not authorized"

    @allure.feature('Add product to basket')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('Testing adding product to cart')
    @pytest.mark.parametrize('payload_product', [
        Data.payload_add_to_basket_product_1,
        Data.payload_add_to_basket_product_2])
    def test_add_product_to_basket(self, payload_product):
        """Checks that one product has been added to the cart first,
        then another."""
        headers = Data.headers
        response = Api(Data.url_add_to_basket).post_requests(
            payload_product, headers)
        item = response.response['data']['items'][0]
        print(f"ID of added product = {item['entityId']}")
        try:
            assert response.status == 200
            assert item['count'] == 1
            assert isinstance(item['count'], int)
            assert 'data' in json.loads(response.text)
        except json.JSONDecodeError:
            assert False, f"Product not added to cart"

    @allure.feature('Invalid request')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step('Testing invalid request adding product to cart')
    def test_invalid_request(self):
        """Checking that if there is an incorrect request to add an item to
        the cart, an error with the desired status will be raised"""
        headers = Data.headers
        data = {}
        response = Api(Data.url_add_to_basket).post_requests(data, headers)
        errors_title = response.response['errors'][0]['title']
        try:
            assert 'errors' in json.loads(response.text)
            assert errors_title == Data.expected_text_title
            assert isinstance(errors_title, str)
            assert response.status == 422
        except json.JSONDecodeError:
            assert False, f"The request did not complete as expected"
