from pages.locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):
    def add_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()

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
