import re
from selenium.webdriver.support.ui import WebDriverWait
from pages.base_page import BasePage
from locators.locators import FeedLocators as L
from config import WAIT


class FeedPage(BasePage):
    def is_open(self):
        return self.visible(L.TITLE).is_displayed()

    def completed_all_time(self):
        return int(self.visible(L.TOTAL).text.replace(" ", ""))

    def completed_today(self):
        return int(self.visible(L.TODAY).text.replace(" ", ""))

    def wait_all_time_increase(self, previous):
        return WebDriverWait(self.driver, WAIT).until(
            lambda _: self.completed_all_time() > previous)

    def wait_today_increase(self, previous):
        return WebDriverWait(self.driver, WAIT).until(
            lambda _: self.completed_today() > previous)

    def wait_order_in_progress(self, order_number):
        target = str(order_number)
        return WebDriverWait(self.driver, WAIT).until(
            lambda _: any(
                int(match.group()) == int(target)
                for item in self.driver.find_elements(*L.IN_PROGRESS)
                if (match := re.search(r"\d+", item.text))
            ))
