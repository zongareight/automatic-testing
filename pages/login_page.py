from .locators import LoginPageLocators
from .base_page import BasePage


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_EMAIL
        ).send_keys(email)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_PASSWORD
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.CONFIRM_PASSWORD
        ).send_keys(password)
        self.browser.find_element(
            *LoginPageLocators.REGISTRATION_SUBMIT
        ).click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert 'login' in self.browser.current_url, 'wrong url for login page'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(
            *LoginPageLocators.LOGIN_FORM
        ), 'Login form is not presented'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(
            *LoginPageLocators.REGISTER_FORM
        ), 'Register form is not presented'
