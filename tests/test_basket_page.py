from pages.main_page import MainPage
from pages.basket_page import BasketPage
from conftest import driver


class TestBasketPage:

    def test_cart_operation(self, driver):
        """Checks that when adding an item to the cart, the quantity and name
        of the goods are displayed."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        basket_page = BasketPage(driver)
        basket_page.select_a_product_and_add_it_to_cart()
        basket_page.go_to_cart()
        basket_page.assert_the_quantity_and_name_of_the_product_are_displayed()

    def test_adding_and_removing_items_to_cart(self, driver):
        """Adds an item to the cart, then removes it and checks that the
        cart is empty."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        basket_page = BasketPage(driver)
        basket_page.select_a_product_and_add_it_to_cart()
        basket_page.go_to_cart()
        basket_page.remove_item_from_cart()
        basket_page.assert_basket_empty()

    def test_add_product_to_favorites(self, driver):
        """Checks that if you click on the "add product to favorites" button
        for a product, then going to the favorites section, this product
        will be displayed."""
        main_page = MainPage(driver)
        main_page.open_page_and_reject_cookies()
        basket_page = BasketPage(driver)
        basket_page.select_a_product_and_add_it_to_cart()
        basket_page.go_to_cart()
        basket_page.add_to_favorites()
        main_page.click_on(main_page.locator_account_button)
        basket_page.click_on(basket_page.FEATURED_PRODUCT_BUTTON_LOCATOR)
        basket_page.assert_product_in_favorites()
