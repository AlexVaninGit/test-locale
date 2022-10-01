import time

from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.base_page import BasePage
from pages.locators import ProductPageLocators
import time
import pytest


#
# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#                                   "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
# def test_guest_can_add_product_to_basket(browser, link):
#     # link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.add_to_basket()
#
#
#
# def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.go_to_basket_page()
#     basket_page = BasketPage(browser=browser, url=browser.current_url)
#     basket_page.text_is_empty_in_basket()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.add_to_basket()
#     page.is_not_element_present(*ProductPageLocators.MESSAGE_NAME_BOOK)
#
#
# def test_guest_cant_see_success_message(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.is_not_element_present(*ProductPageLocators.MESSAGE_NAME_BOOK)
#
#
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
#     page = ProductPage(browser=browser, url=link)
#     page.open()
#     page.add_to_basket()
#     page.is_disappeared(*ProductPageLocators.MESSAGE_NAME_BOOK)


class TestUserAddToBasketFromProductPage:

    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.browser = browser
        self.page = LoginPage(browser=self.browser, url="http://selenium1py.pythonanywhere.com/ru/accounts/login/")
        self.page.open()
        value = str(time.time())
        self.page.register_new_user(email=value + "@fakemail.org", password=value)
        # base_page = BasePage(browser=browser, url=browser.current_url)
        self.page.should_be_authorized_user()

    def test_user_cant_see_success_message(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser=self.browser, url=link)
        page.open()
        page.is_not_element_present(*ProductPageLocators.MESSAGE_NAME_BOOK)

    def test_user_can_add_product_to_basket(self):
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser=self.browser, url=link)
        page.open()
        page.add_to_basket()
