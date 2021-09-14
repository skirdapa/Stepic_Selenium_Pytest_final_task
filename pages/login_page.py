from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # print("текущий урл: ", self.browser.current_url)
        assert "login" in self.browser.current_url, "Это не страница логина: в URL нет слова login"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_INPUT), \
            "Не найдено поле ввода логина в форме авторизации"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), \
            "Не найдено поле ввода пароля в форме авторизации"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME_INPUT), \
            "Не найдено поле ввода логина в форме регистрации"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT), \
            "Не найдено поле ввода пароля в форме регистрации"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT), \
            "Не найдено поле ввода подстверждения пароля в форме регистрации"
