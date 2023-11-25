import logging
import allure
from all_api.models import ResponseModel
from all_api.requests import Client
from all_api.data import Data

logger = logging.getLogger("api")


class Api:
    def __init__(self, url):
        self.url = url
        self.client = Client()

    @allure.feature("Func get requests")
    def get_requests(self, sent_headers=None):
        response = self.client.send_request(
            "GET", self.url, headers=sent_headers)
        logger.info(response)
        return ResponseModel(
            status=response.status_code,
            headers=response.headers,
            request=response.request)

    @allure.feature("Func post requests")
    def post_requests(self, data: dict, headers: dict):
        response = self.client.send_request(
            "POST", f"{self.url}", data=data, headers=headers)
        logger.info(response)
        return ResponseModel(
            status=response.status_code,
            response=response.json(),
            text=response.text)

    @allure.feature("Func authorization user")
    def authorization_user(self, data: dict, headers: dict):
        response = self.client.send_request(
            "POST", f"{self.url}{Data.POST_AUTHORIZATION_USER}", data=data,
            headers=headers)
        logger.info(response)
        return ResponseModel(
            status=response.status_code, response=response.json())
