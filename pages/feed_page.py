import re

from pages.base_page import BasePage
from locators.locators import FeedLocators as L


class FeedPage(BasePage):
    def is_open(self):
        return self.visible(L.TITLE).is_displayed()

    def completed_all_time(self):
        return int(self.get_text(L.TOTAL).replace(" ", ""))

    def completed_today(self):
        return int(self.get_text(L.TODAY).replace(" ", ""))

    def wait_all_time_increase(self, previous):
        return self.until(lambda: self.completed_all_time() > previous)

    def wait_today_increase(self, previous):
        return self.until(lambda: self.completed_today() > previous)

    def wait_order_in_progress(self, order_number):
        target = int(order_number)

        def found():
            return any(
                int(match.group()) == target
                for item in self.elements(L.IN_PROGRESS)
                if (match := re.search(r"\d+", item.text))
            )

        return self.until(found)
