import allure

from helpers import FieldsWebElement, Assertion
from conftest import driver
from locators.basket_locator import BasketLocator


class BasketPage(FieldsWebElement, BasketLocator, Assertion):
    request_text_2 = '6.852.245'
    product_name_text = 'Мышь Razer DeathAdder Essential / RZ01-03850200-' \
                        'R3M1 (белый)'
    expected_text_empty_basket = 'У вас пока нет ни одного товара в корзи' \
                                 'не,\nвы можете выбрать их здесь'
    text_promo = 'СВЯЗЬ'

    def click_on_product(self, product):
        self.click_on(product)

    def enter_product_text(self, product):
        self.click_on(self.CATALOG_SEARCH_LOCATOR)
        self.fill(self.CATALOG_SEARCH_LOCATOR, product)

    @allure.step('Add item to cart')
    def add_item_to_cart(self):
        self.click_on(self.ADD_TO_CART_BUTTON_LOCATOR)

    @allure.step('Go to cart')
    def go_to_cart(self):
        self.click_on(self.BASKET_LOCATOR)

    @allure.step('Count the number of items in the cart')
    def count_the_number_of_items_in_the_cart(self):
        return self.wait_for_visible(self.NUMBER_OF_ITEM_CART_LOCATOR)

    @staticmethod
    @allure.step('Assert the number of items in the cart corresponds to')
    def assert_the_number_of_items_in_the_cart_corresponds_to(
            number_of_goods, expected_result):
        assert int(number_of_goods) == expected_result

    @allure.step('Assert basket empty')
    def assert_basket_empty(self):
        self.assert_text_in_element(
            self.EMPTY_BASKET_LOCATOR, self.expected_text_empty_basket)

    @allure.step('Remove item from cart')
    def remove_item_from_cart(self):
        self.click_on(self.DELETE_BUTTON_LOCATOR)
        self.click_on(self.CONFIRM_DELETE_LOCATOR)

    @allure.step('Select a product and add it to cart')
    def select_a_product_and_add_it_to_cart(self):
        self.enter_product_text(self.request_text_2)
        self.click_on_product(self.CHOOSE_PRODUCT_LOCATOR2)
        self.add_item_to_cart()

    @allure.step('Assert the quantity and name of the product are displayed')
    def assert_the_quantity_and_name_of_the_product_are_displayed(self):
        number_of_goods = self.count_the_number_of_items_in_the_cart().text
        self.assert_the_number_of_items_in_the_cart_corresponds_to(
            number_of_goods, 1
        )
        self.assert_text_in_element(
            self.PRODUCT_IN_THE_CART_LOCATOR,
            self.product_name_text
        )

    @allure.step('Add to favorites')
    def add_to_favorites(self):
        self.click_on(self.ADD_TO_FAVORITES_BUTTON_LOCATOR)

    @allure.step('Assert product in favorites')
    def assert_product_in_favorites(self):
        assert self.product_name_text in self.wait_for_visible(
            self.FEATURED_PRODUCT_LOCATOR).text

    @allure.step('Calculate price before discount')
    def calculate_price_before_discount(self):
        return self.wait_for_visible(self.PRICE_LOCATOR).text

    @allure.step('Enter the promotional code and confirm')
    def enter_the_promotional_code_and_confirm(self):
        self.fill(self.FIELD_FOR_ENTERING_PROMO_LOCATOR, self.text_promo)
        self.click_on(self.CONFIRM_PROMO_BUTTON_LOCATOR)

    @allure.step('Calculate price after discount')
    def calculate_price_after_discount(self):
        self.wait_for_element_to_change(self.PRICE_LOCATOR, '99,31')
        return self.wait_for_visible(self.PRICE_LOCATOR).text

    @allure.step('Assert the price has decreased')
    def assert_the_price_has_decreased(self):
        assert int(self.calculate_price_before_discount()) > \
               int(self.calculate_price_after_discount())
