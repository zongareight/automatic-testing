from selenium.webdriver.common.by import By


class BasePageLocators:
    CART_LINK = (By.CSS_SELECTOR, 'div.basket-mini>.btn-group>a.btn.btn-default')
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, '#login_link_inc')


class CartPageLocators:
    BASKET_FORMSET = (By.CSS_SELECTOR, '#basket-formset')
    CONTENT_INNER = (By.CSS_SELECTOR, '#content_inner')


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h1')
    PRODUCT_NAME_IN_MESSAGE = (
        By.CSS_SELECTOR, '#messages .alertinner  strong'
    )
    PRODUCT_PRICE_IN_MESSAGE = (
        By.CSS_SELECTOR, '#messages .alert-info strong'
    )
