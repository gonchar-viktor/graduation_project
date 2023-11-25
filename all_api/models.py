from data import TEST_USER
import json


class AuthorizationUser:
    @staticmethod
    def user_data():
        return json.dumps({
            "User": {
                "email": TEST_USER.get('email'),
                "password": TEST_USER.get('password')
            }
        })


class ResponseModel:
    def __init__(self, status: int, headers=None, request=None, text=None,
                 response: dict = None):
        self.status = status
        self.response = response
        self.headers = headers
        self.request = request
        self.text = text
