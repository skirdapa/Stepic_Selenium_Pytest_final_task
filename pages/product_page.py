from pages.base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def should_be_add_to_basket_message(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_MESSAGE), \
            "Отсутствует сообщение о добавлении в корзину"

    def should_be_basket_cost_message(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_COST_MESSAGE), \
            "Отсутствует сообщение о стоимости корзины"

    def should_be_basket_cost_is_right(self):
        self.should_be_basket_cost_message()
        basket_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_MESSAGE).text
        product_cost = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_ON_PAGE).text
        assert basket_cost == product_cost, "Стоимость корзины не совпадает с ценой товара"

    def should_be_product_title_in_basket_is_right(self):
        self.should_be_add_to_basket_message()
        product_title_on_page = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_ON_PAGE).text
        product_title_in_basket = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE_IN_MESSAGE).text
        assert product_title_in_basket == product_title_on_page, \
            "Название товара в корзине не совпадает с названием товара на странице"



