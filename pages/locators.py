from selenium.webdriver.common.by import By


class BasePageLocators:
    CART_LINK = (
        By.CSS_SELECTOR,
        'div.basket-mini > .btn-group > a.btn.btn-default'
    )
    LOGIN_LINK = (By.ID, 'login_link')
    LOGIN_LINK_INVALID = (By.ID, 'login_link_inc')
    USER_ICON = (By.CSS_SELECTOR, '.icon-user')


class CartPageLocators:
    BASKET_FORMSET = (By.ID, 'basket-formset')
    CONTENT_INNER = (By.ID, 'content_inner')


class MainPageLocators:
    LOGIN_LINK = (By.ID, 'login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTRATION_PASSWORD = (By.ID, 'id_registration-password1')
    CONFIRM_PASSWORD = (By.ID, 'id_registration-password2')
    REGISTRATION_SUBMIT = (By.NAME, 'registration_submit')
    REGISTRATION_EMAIL = (By.ID, 'id_registration-email')
    REGISTER_FORM = (By.ID, 'register_form')


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
