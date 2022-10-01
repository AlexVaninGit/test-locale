from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, f"login in not {self.browser.current_url}"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_element = self.browser.find_element(*LoginPageLocators.EMAIL_INPUT)
        email_element.send_keys(email)
        password_element = self.browser.find_element(*LoginPageLocators.PASSWORD_INPUT)
        password_element.send_keys(password)
        confirm_password = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_INPUT)
        confirm_password.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.REGISTER_BTN)
        button.click()



