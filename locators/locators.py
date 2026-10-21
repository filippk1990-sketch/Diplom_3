"""Selenium selectors used by Page Object classes."""

from selenium.webdriver.common.by import By


def xpath_literal(value):
    """Quote a text value safely for an XPath expression."""
    if "'" not in value:
        return "'" + value + "'"
    if '"' not in value:
        return '"' + value + '"'
    return 'concat(' + ', "\'", '.join("'" + part + "'" for part in value.split("'")) + ')'


class HeaderLocators:
    CONSTRUCTOR = (By.XPATH, '//a[@href="/"][contains(normalize-space(.),"Конструктор")]')
    FEED = (By.XPATH, '//a[@href="/feed"][contains(normalize-space(.),"Лента")]')


class ConstructorLocators:
    TITLE = (By.XPATH, '//h1[normalize-space()="Соберите бургер"]')
    FIRST_INGREDIENT = (By.CSS_SELECTOR, 'a[class*="BurgerIngredient_ingredient"]')
    INGREDIENT_BY_NAME = (
        '//a[contains(@class,"BurgerIngredient_ingredient")]'
        '[.//p[normalize-space()={}]]'
    )
    INGREDIENT_COUNTER = (By.CSS_SELECTOR, '[class*="counter_counter__num"]')
    MODAL = (By.CSS_SELECTOR, 'section[class*="Modal_modal_opened"]')
    MODAL_TITLE = (By.XPATH, '//h2[normalize-space()="Детали ингредиента"]')
    MODAL_CLOSE = (
        By.CSS_SELECTOR,
        'section[class*="Modal_modal_opened"] button[class*="Modal_modal__close"]',
    )
    BASKET = (
        By.CSS_SELECTOR,
        'section[class*="BurgerConstructor_basket"], ul[class*="BurgerConstructor_basket"]',
    )
    PLACE_ORDER = (By.XPATH, '//button[normalize-space()="Оформить заказ"]')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'h2[class*="Modal_modal__title_shadow"]')
    ORDER_CLOSE = (
        By.CSS_SELECTOR,
        'section[class*="Modal_modal_opened"] button[class*="Modal_modal__close"]',
    )

    @classmethod
    def ingredient_by_name(cls, name):
        return By.XPATH, cls.INGREDIENT_BY_NAME.format(xpath_literal(name))


class LoginLocators:
    EMAIL = (By.CSS_SELECTOR, 'input[name="name"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[type="password"]')
    SUBMIT = (By.XPATH, '//form//button[normalize-space()="Войти"]')


class FeedLocators:
    TITLE = (By.XPATH, '//h1[normalize-space()="Лента заказов"]')
    TOTAL = (By.XPATH, '//p[contains(text(),"Выполнено за все время")]/following-sibling::p[1]')
    TODAY = (By.XPATH, '//p[contains(text(),"Выполнено за сегодня")]/following-sibling::p[1]')
    IN_PROGRESS = (By.CSS_SELECTOR, 'ul[class*="OrderFeed_orderListReady"] li')
