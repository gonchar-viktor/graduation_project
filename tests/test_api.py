import allure
import pytest
import requests
import json

from data import DOMAIN
from elements.api import Api


class TestApi:
    api = Api

    @allure.feature("Main page")
    @allure.severity(allure.severity_level.BLOCKER)
    @allure.step('Testing status and output of the request time')
    def test_main_page(self):
        response = requests.get(DOMAIN)
        print(f"\n{response.headers['date']}")
        try:
            assert response.status_code == 200
        except json.JSONDecodeError:
            assert False, f"Status code = {response.status_code}"

    @allure.feature('Main elements of the page')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('Testing status and request method')
    def test_main_elements_of_the_page(self):
        """Checks the request status and request method of the main elements
        on the page"""
        api = Api
        for url in api.urls_main_elements_of_the_page:
            response = requests.get(
                url, headers=api.headers
            )
            print(f"Status code = {response.status_code}")
            print(f"request = {response.request}")
            try:
                assert response.status_code == 200 and \
                       '<PreparedRequest [GET]>' == f'{response.request}'
            except json.JSONDecodeError:
                assert False, f"The status code or request method is not " \
                              f"correct"

    @allure.feature('Login user')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('Testing login user and his name')
    def test_login(self):
        """Checks the user's authorization on the site, and checks that the
        username is correct"""
        api = Api
        response = requests.post(
            api.url_users_login,
            headers=api.headers_user_login,
            data=api.payload_user_data
        )
        response_json = response.json()['user']['name']
        print(f"\nUsername is  = '{response_json}'")
        try:
            assert response_json == 'test user name'
        except json.JSONDecodeError:
            assert False, f"User is not authorized"

    @allure.feature('Add product to basket')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.step('Testing adding product to cart')
    @pytest.mark.parametrize('payload_product', [
        api.payload_add_to_basket_product_1,
        api.payload_add_to_basket_product_2])
    def test_add_product_to_basket(self, payload_product):
        """Checks that one product has been added to the cart first,
        then another."""
        api = Api
        response = requests.post(
            api.url_add_to_basket,
            headers=api.headers,
            data=payload_product
        )
        response_json = response.json()['data']['items']
        print(f"ID of added product = {response_json[0]['entityId']}")
        try:
            assert response_json[0]['count'] == 1 and 'data' in json.loads(
                response.text)
        except json.JSONDecodeError:
            assert False, f"Product not added to cart"

    @allure.feature('Invalid request')
    @allure.severity(allure.severity_level.NORMAL)
    @allure.step('Testing invalid request adding product to cart')
    def test_invalid_request(self):
        """Checking that if there is an incorrect request to add an item to
        the cart, an error with the desired status will be raised"""
        api = Api
        response = requests.post(
            api.url_add_to_basket,
            headers=api.headers
        )
        try:
            assert 'errors' in json.loads(response.text) and response.json()[
                'errors'][0]['title'] == api.expected_text_title and \
                   response.status_code == 422
        except json.JSONDecodeError:
            assert False, f"The request did not complete as expected"
