import requests
from requests import Response


class Client:
    @staticmethod
    def send_request(method: str, url: str, **kwargs) -> Response:
        """
        Request method: method for the new Request object: GET, OPTIONS, HEAD,
        POST, PUT, PATCH, or DELETE.
        """
        return requests.request(method, url, **kwargs)
