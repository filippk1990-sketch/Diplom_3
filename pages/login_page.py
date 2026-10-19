from pages.base_page import BasePage
from locators.locators import LoginLocators as L
from locators.locators import ConstructorLocators


class LoginPage(BasePage):
    def login(self, user):
        self.open("/login")
        self.visible(L.EMAIL).send_keys(user["email"])
        self.visible(L.PASSWORD).send_keys(user["password"])
        self.click(L.SUBMIT)
        self.visible(ConstructorLocators.TITLE)
