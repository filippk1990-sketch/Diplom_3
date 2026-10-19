from selenium.webdriver.common.by import By


class HeaderLocators:
    CONSTRUCTOR = (By.XPATH, '//a[@href="/"][contains(normalize-space(.),"Конструктор")]')
    FEED = (By.XPATH, '//a[@href="/feed"][contains(normalize-space(.),"Лента")]')


class ConstructorLocators:
    TITLE = (By.XPATH, '//h1[normalize-space()="Соберите бургер"]')
    FIRST_INGREDIENT = (By.CSS_SELECTOR, 'a[class*="BurgerIngredient_ingredient"]')
    MODAL = (By.CSS_SELECTOR, 'section[class*="Modal_modal_opened"]')
    MODAL_TITLE = (By.XPATH, '//h2[normalize-space()="Детали ингредиента"]')
    MODAL_CLOSE = (By.CSS_SELECTOR, 'section[class*="Modal_modal_opened"] button[class*="Modal_modal__close"]')
    BASKET = (By.CSS_SELECTOR, 'ul[class*="BurgerConstructor_basket"]')
    PLACE_ORDER = (By.XPATH, '//button[normalize-space()="Оформить заказ"]')
    ORDER_NUMBER = (By.CSS_SELECTOR, 'h2[class*="Modal_modal__title_shadow"]')
    ORDER_CLOSE = (By.CSS_SELECTOR, 'button[class*="Modal_modal__close"]')


class LoginLocators:
    EMAIL = (By.CSS_SELECTOR, 'input[name="name"]')
    PASSWORD = (By.CSS_SELECTOR, 'input[type="password"]')
    SUBMIT = (By.XPATH, '//form//button[normalize-space()="Войти"]')


class FeedLocators:
    TITLE = (By.XPATH, '//h1[normalize-space()="Лента заказов"]')
    TOTAL = (By.XPATH, '//p[contains(text(),"Выполнено за все время")]/following-sibling::p[1]')
    TODAY = (By.XPATH, '//p[contains(text(),"Выполнено за сегодня")]/following-sibling::p[1]')
    IN_PROGRESS = (By.CSS_SELECTOR, 'ul[class*="OrderFeed_orderListReady"] li')
