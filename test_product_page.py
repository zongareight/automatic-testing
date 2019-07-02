import pytest
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from pages.login_page import LoginPage
# parameters list for test_guest_can_add_product_to_cart
base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
links = [f"{base_link}/?promo=offer{n}" for n in range(10)]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_cart(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    name = page.get_product_name()
    price = page.get_product_price()
    msg_name = page.get_product_name_from_message()
    msg_price = page.get_product_price_from_message()
    assert msg_name == name, f'Product name is wrong: {link}'
    assert msg_price == price, f'Product price is wrong: {link}'


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_209"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = f"http://selenium1py.pythonanywhere.com" \
        f"/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = f"http://selenium1py.pythonanywhere.com" \
        f"/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.news
def test_guest_cant_see_product_in_cart_opened_from_product_page(browser):
    link = f"http://selenium1py.pythonanywhere.com" \
        f"/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cart_link()
    page.go_to_cart_page()
    cart_page = CartPage(browser, browser.current_url)
    cart_page.should_be_cart_page()
    cart_page.should_not_be_products_in_cart()
    cart_page.should_be_message_about_empty_cart()
