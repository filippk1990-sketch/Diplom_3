import re

from pages.base_page import BasePage
from locators.locators import ConstructorLocators as L


class ConstructorPage(BasePage):
    def is_open(self):
        return self.visible(L.TITLE).is_displayed()

    def first_ingredient(self):
        return self.visible(L.FIRST_INGREDIENT)

    def open_ingredient_details(self):
        self.click_element(self.first_ingredient())
        return self.get_text(L.MODAL_TITLE)

    def is_details_modal_open(self):
        return self.visible(L.MODAL).is_displayed()

    def is_details_modal_closed(self):
        return self.is_hidden(L.MODAL)

    def close_modal(self):
        self.click(L.MODAL_CLOSE)
        self.wait_for_invisibility(L.MODAL)

    def ingredient_by_name(self, name):
        return self.visible(L.ingredient_by_name(name))

    def ingredient_count(self, ingredient_name):
        card = self.ingredient_by_name(ingredient_name)
        counters = self.child_elements(card, L.INGREDIENT_COUNTER)
        if not counters:
            return 0
        value = counters[0].text.strip() or (
            counters[0].get_attribute("textContent") or ""
        ).strip()
        return int(value) if value else 0

    def wait_ingredient_count(self, ingredient_name, expected):
        return self.until(
            lambda: self.ingredient_count(ingredient_name) == expected
        )

    def add_to_basket(self, ingredient_name):
        self.drag_to(
            self.ingredient_by_name(ingredient_name),
            self.visible(L.BASKET),
        )

    def order(self):
        self.click(L.PLACE_ORDER)

        def final_order_number():
            text = self.get_text(L.ORDER_NUMBER).strip()
            match = re.search(r"\d+", text)
            if not match:
                return False
            number = int(match.group())
            # The real UI uses 9999 as a temporary loading placeholder.
            return number if number > 0 and number != 9999 else False

        return self.until(final_order_number)

    def close_order(self):
        self.click(L.ORDER_CLOSE)
        self.wait_for_invisibility(L.MODAL)
