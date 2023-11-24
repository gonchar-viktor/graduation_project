# from urllib.parse import urljoin
# # from aiohttp import ClientSession
# # from config import HEADERS_ACCEPT_TEXT, HOST_URL
# from dataclasses import dataclass, field
#
#
# @dataclass
# class HttpBin:
#     session: ClientSession = field(init=True, default_factory=ClientSession)
#
#     async def get_status(self, status: str):
#         """
#         Get specific status.
#         :param status: code
#         :return: response
#         """
#         endpoint = f"/status/{status}"
#         url = urljoin(HOST_URL, endpoint)
#         headers = {"accept": HEADERS_ACCEPT_TEXT}
#         response = await self.session.get(url, headers=headers)
#         return response
#
#     async def post_response_headers(self, freeform: str):
#         """
#         Set response headers
#         :param freeform: free text
#         :return: response
#         """
#         endpoint = f"/response-headers"
#         url = urljoin(HOST_URL, endpoint)
#         params = {"freeform": freeform}
#         headers = {"accept": HEADERS_ACCEPT_TEXT}
#         response = await self.session.post(url, headers=headers, params=params)
#         return response
#
#     async def redirect(self, n: str):
#         """
#         Redirect user on page "https://httpbin.org/"
#         :param n: amount redirects
#         :return: response and redirect_url
#         """
#         endpoint = f"/redirect/{n}"
#         url = urljoin(HOST_URL, endpoint)
#         headers = {"accept": HEADERS_ACCEPT_TEXT}
#         response = await self.session.get(url, headers=headers)
#         content = await response.json(content_type=None)
#         redirect_url = content["url"]
#         return response, redirect_url
#
#     async def close(self) -> None:
#         """
#         Close session
#         """
#         await self.session.close()