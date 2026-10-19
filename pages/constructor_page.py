import re
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import ConstructorLocators as L


class ConstructorPage(BasePage):
    def is_open(self):
        return self.visible(L.TITLE).is_displayed()

    def first_ingredient(self):
        return self.visible(L.FIRST_INGREDIENT)

    def open_ingredient_details(self):
        self.first_ingredient().click()
        return self.visible(L.MODAL_TITLE).text

    def is_details_modal_open(self):
        return self.visible(L.MODAL).is_displayed()

    def close_modal(self):
        self.click(L.MODAL_CLOSE)
        self.wait.until(EC.invisibility_of_element_located(L.MODAL))

    def ingredient_by_name(self, name):
        # Ingredients are links and use the actual label from API, not hardcoded nth positions.
        return self.visible((By.XPATH,
            '//a[contains(@class,"BurgerIngredient_ingredient")][.//p[normalize-space()='+
            self._xpath_literal(name)+']]'))

    @staticmethod
    def _xpath_literal(value):
        if "'" not in value:
            return "'" + value + "'"
        if '"' not in value:
            return '"' + value + '"'
        return 'concat(' + ', "\'", '.join("'" + x + "'" for x in value.split("'")) + ')'

    def ingredient_count(self, ingredient_name):
        card = self.ingredient_by_name(ingredient_name)
        counters = card.find_elements(By.CSS_SELECTOR, '[class*="counter_counter__num"]')
        if not counters:
            return 0
        value = counters[0].text.strip() or (counters[0].get_attribute("textContent") or "").strip()
        return int(value) if value else 0

    def add_to_basket(self, ingredient_name):
        card = self.ingredient_by_name(ingredient_name)
        target = self.visible(L.BASKET)
        self.driver.execute_script('arguments[0].scrollIntoView({block:"center"})', card)
        ActionChains(self.driver).click_and_hold(card).pause(0.5).move_to_element(target).pause(0.7).release().perform()

    def order(self):
        self.click(L.PLACE_ORDER)
        self.wait.until(lambda d: re.search(r"\d+", self.visible(L.ORDER_NUMBER).text))
        return int(re.search(r"\d+", self.visible(L.ORDER_NUMBER).text).group())

    def close_order(self):
        self.click(L.ORDER_CLOSE)
        self.wait.until(EC.invisibility_of_element_located(L.MODAL))
