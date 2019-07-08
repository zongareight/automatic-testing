from pages.locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

    def added_product_name_is_correct(self):
        name = self.get_product_name()
        name_from_message = self.get_product_name_from_message()
        assert name == name_from_message, 'Product name is wrong'

    def added_product_price_is_correct(self):
        price = self.get_product_price()
        price_from_message = self.get_product_price_from_message()
        assert price == price_from_message, 'Product price is wrong'

    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def get_product_name_from_message(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE
        ).text

    def get_product_price_from_message(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE
        ).text

    def should_not_be_success_message(self):
        assert self.is_not_element_present(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(
            *ProductPageLocators.SUCCESS_MESSAGE
        ), "Success message not disappeared"
