from data import DOMAIN
from helpers.assertions import Assertion
import requests
import json


class Api:

    urls_main_elements_of_the_page = {
        'https://gate.21vek.by/ecart/v2/ecarts/meta',
        f'{DOMAIN}users/session/office/',
        f'{DOMAIN}users/me/',
        'https://gate.21vek.by/index/v1/special-offers?type=all',
        'https://gate.21vek.by/index/v1/popular',
        'https://gate.21vek.by/index/v1/videos',
        'https://gate.21vek.by/cart/carts.info',
        'https://gate.21vek.by/cart/carts.meta'
    }

    headers_main_elements_of_the_page = {
        "Accept": "application/json",
        "Connection": "keep-alive",
        "Content-Type": "application/json"
    }


