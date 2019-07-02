from pages.locators import CartPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    def should_be_cart_page(self):
        assert 'basket' in self.browser.current_url, 'wrong url for cart page'

    def should_not_be_products_in_cart(self):
        assert self.is_not_element_present(
            *CartPageLocators.BASKET_FORMSET
        ), 'products are in cart, but should not be'

    def should_be_message_about_empty_cart(self):
        assert self.is_element_present(
            *CartPageLocators.CONTENT_INNER
        ), 'there should be a message about an empty basket, but it is not'
