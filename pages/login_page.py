from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        """Регистрируем нового пользователя

        :param email: валидный email адрес
        :param password: пароль длиннее 9 символов, с буквой, цифрой
        """
        email_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_USERNAME_INPUT)
        email_input.send_keys(email)
        password_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT)
        password_input.send_keys(password)
        password_confirm_input = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT)
        password_confirm_input.send_keys(password)
        button_submit = self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON)
        button_submit.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Это не страница логина: в URL нет слова login"

    def should_be_login_form(self):
        # проверка, что есть форма авторизации на странице
        assert self.is_element_present(*LoginPageLocators.LOGIN_USERNAME_INPUT), \
            "Не найдено поле ввода логина в форме авторизации"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD_INPUT), \
            "Не найдено поле ввода пароля в форме авторизации"

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_USERNAME_INPUT), \
            "Не найдено поле ввода логина в форме регистрации"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_INPUT), \
            "Не найдено поле ввода пароля в форме регистрации"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_INPUT), \
            "Не найдено поле ввода подстверждения пароля в форме регистрации"
