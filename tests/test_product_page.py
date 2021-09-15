import pytest

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


@pytest.mark.xfail(reason="Заведомо падающий тест, сообщение об ошибке должно появиться")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message_not_present()


def test_guest_cant_see_success_message(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.should_not_be_success_message_not_present()


@pytest.mark.xfail(reason="Заведомо падающий тест, сообщение об ошибке не исчезнет")
def test_message_disappeared_after_adding_product_to_basket(browser):
    product_page = ProductPage(browser, link_without_promo)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message_is_disappeared()

