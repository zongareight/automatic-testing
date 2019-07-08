import time
import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage


@pytest.mark.need_review
def test_guest_can_add_product_to_cart(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    # page.solve_quiz_and_get_code()
    page.added_product_name_is_correct()
    page.added_product_price_is_correct()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()
    cart_page.should_not_be_products_in_cart()
    cart_page.should_be_message_about_empty_cart()


class TestUserAddToCartFromProductPage:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, browser):
        link = f"http://selenium1py.pythonanywhere.com/en-gb/accounts/login"
        email = f'{time.time()}@fakemail.org'
        password = 'very nice'
        page = LoginPage(browser, link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_cart(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/" \
               "coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.add_to_basket()
        # page.solve_quiz_and_get_code()
        page.added_product_name_is_correct()
        page.added_product_price_is_correct()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/" \
               "coders-at-work_207"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
