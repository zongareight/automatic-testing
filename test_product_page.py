import time
from pages.product_page import ProductPage


def test_guest_can_add_product_to_cart(browser):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    cena = browser.find_element_by_css_selector('p.price_color').text
    print(cena.split()[0])
    time.sleep(20)
