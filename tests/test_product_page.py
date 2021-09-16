import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

links = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
         pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                      marks=pytest.mark.xfail(reason="Не будут править")),
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
         "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


@pytest.mark.parametrize('link', links)
def test_guest_can_add_product_to_basket(browser, link):
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_be_basket_cost_is_right()
    product_page.should_be_product_title_in_basket_is_right()


link_without_promo = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"


@pytest.mark.xfail(reason="Заведомо падающий тест, сообщение об ошибке и должно появиться")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message_not_present()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.should_not_be_success_message_not_present()


@pytest.mark.xfail(reason="Заведомо падающий тест, сообщение об ошибке и не исчезнет")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message_is_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.empty_basket
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_product_not_exists()
    basket_page.should_be_product_not_exists()

