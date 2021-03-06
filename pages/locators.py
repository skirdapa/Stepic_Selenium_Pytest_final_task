from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_invalid")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a[href]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")
    BASKET_IS_EMPTY_TEXT = (By.CSS_SELECTOR, "#content_inner > p")


class MainPageLocators:
    pass


class LoginPageLocators:
    LOGIN_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_login-username")
    LOGIN_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_login-password")
    REGISTRATION_USERNAME_INPUT = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTRATION_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTRATION_CONFIRM_PASSWORD_INPUT = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTRATION_SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[name=registration_submit]")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_TITLE_ON_PAGE = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_TITLE_IN_MESSAGE = (By.CSS_SELECTOR, "#messages div:first-child strong")
    PRODUCT_PRICE_ON_PAGE = (By.CSS_SELECTOR, ".product_main p.price_color")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    ADD_TO_BASKET_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    BASKET_COST_MESSAGE = (By.CSS_SELECTOR, ".alert-info")
