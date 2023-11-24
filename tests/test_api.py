import allure
import pytest
import requests
import json

from data import DOMAIN
from elements.api import Api
from conftest import driver


class TestApi:

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
                url, headers=api.headers_main_elements_of_the_page
            )
            try:
                assert response.status_code == 200 and \
                       '<PreparedRequest [GET]>' == f'{response.request}'
            except json.JSONDecodeError:
                assert False, f"Status code = {response.status_code}, " \
                              f"request = {response.request}"






    def test_fhgfdg(self):
        url = 'https://www.21vek.by/users/action/login/'
        payload = json.dumps({
            "User": {
                "email": "test_user_000@mail.ru",
                "password": "9d1ea216"
            }
        })

        headers = {
            'X-Requested-With': 'XMLHttpRequest',
            'Content-Type': 'application/json'
        }
        response = requests.post(url, headers=headers, data=payload)

        response_json = response.json()['user']
        name_user = response_json['name']
        print(f"\nUsername is  = '{name_user}'")

        try:
            assert name_user == 'test user name'
        except json.JSONDecodeError:
            assert False, f"Username is incorrect"









    # def test_dsfgs(self):
    #     headers = {
    #         "Accept": "application/json"
    #     }
    #     url = 'https://gate.21vek.by/index/v1/popular'
    #     response = requests.get(url, headers=headers)
    #     assert response.status_code == 200




    @pytest.mark.asyncio
    @allure.feature("Testing status")
    @pytest.mark.parametrize("status", [200, 300, 400, 500])
    async def test_status(self, status, prepare_for_test, logger):
        """
        Test endpoint /status/:code.
        :param status: status
        :param prepare_for_test: fixture create session
        :param logger: fixture logging
        """
        httpbin = prepare_for_test
        with allure.step("Get status " + str(status)):
            response = await httpbin.get_status(str(status))
            logger.info(response)
            assert response.status == status
            await httpbin.close()



            for url in ['/trtr', 'fdsf']:
                pass

    def test_1(self):
        headers = {
            'Date': 'Wed, 22 Nov 2023 19:03:32 GMT',
            'Content-Length': '0',
            'Connection': 'keep-alive',
            'Allow': 'POST',
            'Strict-Transport-Security': 'max-age=15724800; includeSubDomains'
        }

        url = 'https://ch.21vek.by/collect/v1/t'

        response = requests.post(url, headers=headers)

        print('\nresponse: ', response)
        print('\nheaders: ', response.headers)
        print('\nrequest: ', response.request)
        print('\ntext: ', response.text)
        print('\nstatus: ', response.status_code)

        # js = response.json()
        # print(js)

    def test_11(self):
        headers = {
            'Date': 'Wed, 22 Nov 2023 19:03:32 GMT',
            'Content-Length': '0',
            'Connection': 'keep-alive',
            'Allow': 'POST',
            'Strict-Transport-Security': 'max-age=15724800; includeSubDomains'
        }

        url = 'https://ch.21vek.by/collect/v1/t'
        response = requests.post(url, headers=headers)
        print(response)

        try:
            assert response.status_code == 200
        except json.JSONDecodeError:
            assert False, f"Error"
