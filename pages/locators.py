from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-add-to-basket')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'h1')
    PRODUCT_NAME_IN_MESSAGE = (
        By.CSS_SELECTOR, '#messages .alertinner  strong'
    )
    PRODUCT_PRICE_IN_MESSAGE = (
        By.CSS_SELECTOR, '#messages .alert-info strong'
    )
