from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_basket_btn = self.browser.find_element(*ProductPageLocators.BTN_ADD_TO_BASKET)
        name = self.browser.find_element(*ProductPageLocators.BOOK_NAME).text
        price = self.browser.find_element(*ProductPageLocators.BOOK_PRICE).text
        add_basket_btn.click()
        self.solve_quiz_and_get_code()
        self.browser.implicitly_wait(13)
        name_added = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_BOOK).text
        price_added = self.browser.find_element(*ProductPageLocators.MESSAGE_PRICE_BOOK).text
        assert name == name_added and price == price_added, f'Expected name={name}, price={price}, actual name={name_added}, price={price_added}'


