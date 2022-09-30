from .base_page import BasePage
from .locators import BasketLocators


class BasketPage(BasePage):
    def text_is_empty_in_basket(self):
        emty_text = self.browser.find_element(*BasketLocators.TEXT_IS_EMPTY).text
        self.is_not_element_present(*BasketLocators.BASKET_ITEMS)
        assert "basket is empty" in emty_text, 'text "basket is empty" not found'