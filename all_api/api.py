import logging
import requests

from all_api.data import *
from data import DOMAIN


class Api:

    @staticmethod
    def logger():
        return logging.getLogger("api")

    @staticmethod
    def get_response_main_page():
        response = requests.get(url=DOMAIN)
        Api.logger().info(response)
        return response

    @staticmethod
    def get_status(response):
        status = response.status_code
        Api.logger().info(status)
        return status

    @staticmethod
    def assert_request_status(response, expected_status):
        assert Api.get_status(response) == expected_status, \
            f"Error, requests status = {Api.get_status(response)} != " \
            f"expected requests status = {expected_status}"

    @staticmethod
    def get_response_main_elements():
        list_response = []
        for url in Urls.urls_main_elements_of_the_page:
            response = requests.get(url=url, headers=Headers.headers)
            Api.logger().info(response)
            list_response.append(response)
        return list_response

    @staticmethod
    def assert_request_status_of_all_items(response):
        for i in response:
            assert Api.get_status(i) == 200, \
                f"Error, requests status = {Api.get_status(i)}"

    @staticmethod
    def assert_requests_method_is_get_all_items(response):
        for i in response:
            assert f"{i.request}" == '<PreparedRequest [GET]>', \
                f"Error, requests method is '{i.request}'"

    @staticmethod
    def post_request_authorization():
        response = requests.post(
            url=f"{DOMAIN}{Urls.POST_AUTHORIZATION_USER}",
            data=AuthorizationUser.user_data(),
            headers=Headers.headers_user_login
        )
        Api.logger().info(response)
        return response

    @staticmethod
    def get_user_name(response):
        user_name = response.json()['user']['name']
        Api.logger().info(user_name)
        return user_name

    @staticmethod
    def assert_that_the_user_name_is_correct(user_name):
        assert user_name == 'test user name', \
            f"Error, user name is '{user_name}'"

    @staticmethod
    def assert_whether_the_object_is_of_type_string(param):
        assert isinstance(param, str), \
            f"Error, type object is '{type(param)}'"

    @staticmethod
    def post_request_add_item_to_cart(data_product):
        response = requests.post(
            url=Urls.url_add_to_basket,
            data=data_product,
            headers=Headers.headers
        )
        Api.logger().info(response)
        return response

    @staticmethod
    def get_item_from_cart(response):
        item = response.json()['data']['items'][0]
        Api.logger().info(item)
        return item

    @staticmethod
    def get_count_item_from_cart(item):
        count = item['count']
        Api.logger().info(item['count'])
        return count

    @staticmethod
    def assert_whether_the_object_is_of_type_integer(param):
        assert isinstance(param, int), \
            f"Error, type object is '{type(param)}'"

    @staticmethod
    def assert_that_the_parameter_is_in_the_response(response, param):
        assert f"{param}" in json.loads(response.text), \
            f"Parameter {param} is not in the response"

    @staticmethod
    def get_text_error(response):
        text_error = response['errors'][0]['title']
        Api.logger().info(text_error)
        return text_error

    @staticmethod
    def assert_text_error(expected_text_error, text_error):
        assert expected_text_error == text_error, \
            f"Error, expected text error = {expected_text_error} != " \
            f"text error = {text_error}"
