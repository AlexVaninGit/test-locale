from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators:
    BTN_ADD_TO_BASKET = (By.CLASS_NAME, 'btn-add-to-basket')
    BOOK_NAME = (By.CSS_SELECTOR, '.product_main h1')
    BOOK_PRICE = (By.CLASS_NAME, 'price_color')
    MESSAGE_NAME_BOOK = (By.CSS_SELECTOR, '#messages>div .alertinner>strong')
    MESSAGE_PRICE_BOOK = (By.CSS_SELECTOR, '#messages .alert-info strong')