import pytest

from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.main_page import MainPage

link = "http://selenium1py.pythonanywhere.com/"


@pytest.mark.login_quest
class TestLoginFromMainPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        # Подготавливаем тестовые данные для каждого теста в этом классе (scope="function")
        # Выполняться фикстура будет автоматически (autouse=True)
        yield  # Возвращаем что-то
        # Выполняется после выполнения теста, обычно удаляя тестовые данные, подчищая мусор

    def test_guest_should_see_login_link(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page(self, browser):
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


@pytest.mark.empty_basket
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_product_not_exists()
    basket_page.should_be_basket_is_empty_text()

