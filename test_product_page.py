import time
from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    name = page.get_product_name()
    price = page.get_product_price()
    msg_name = page.get_product_name_from_message()
    msg_price = page.get_product_price_from_message()
    assert msg_name == name, ''
    assert msg_price == price, ''
    time.sleep(8)
