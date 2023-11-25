from data import DOMAIN
import json


class Data:
    """
    Class for storing data used for API tests: urls, headers, body and text
    """
    # urls

    POST_AUTHORIZATION_USER = 'users/action/login/'

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

    url_users_login = f'{DOMAIN}users/action/login/'

    url_add_to_basket = "https://gate.21vek.by/cart/carts/items"

    # headers

    headers_user_login = {
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/json'
    }

    headers = {
        "Accept": "application/json",
        "Connection": "keep-alive",
        "Content-Type": "application/json"
    }

    # body

    payload_add_to_basket_product_1 = json.dumps({
        "id": 5682444,
        "type": "product"
    })
    payload_add_to_basket_product_2 = json.dumps({
        "id": 8233771,
        "type": "product"
    })

    # text

    expected_text_title = 'Поле type должно быть заполнено'
