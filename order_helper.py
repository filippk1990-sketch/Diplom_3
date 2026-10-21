"""Business flows used by feed tests, kept separate from test modules."""

from pages.constructor_page import ConstructorPage
from pages.login_page import LoginPage


def place_new_order(driver, user, menu):
    LoginPage(driver).login(user)
    constructor = ConstructorPage(driver)
    constructor.add_to_basket(menu["bun"])
    constructor.add_to_basket(menu["filling"])
    number = constructor.order()
    constructor.close_order()
    return number
