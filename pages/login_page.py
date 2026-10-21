from pages.base_page import BasePage
from locators.locators import ConstructorLocators, LoginLocators as L


class LoginPage(BasePage):
    def login(self, user):
        self.open("/login")
        self.enter_text(L.EMAIL, user["email"])
        self.enter_text(L.PASSWORD, user["password"])
        self.click(L.SUBMIT)
        self.visible(ConstructorLocators.TITLE)
