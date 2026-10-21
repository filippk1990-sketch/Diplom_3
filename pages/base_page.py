"""Shared Selenium operations: page classes never access WebDriver directly."""

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, WAIT
from locators.locators import HeaderLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT)

    def open(self, path="/"):
        self.driver.get(f"{BASE_URL}{path}")

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def click_element(self, element):
        element.click()

    def enter_text(self, locator, value):
        self.visible(locator).send_keys(value)

    def get_text(self, locator):
        return self.visible(locator).text

    def elements(self, locator):
        return self.driver.find_elements(*locator)

    def child_elements(self, parent, locator):
        return parent.find_elements(*locator)

    def is_hidden(self, locator):
        return all(not element.is_displayed() for element in self.elements(locator))

    def wait_for_invisibility(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def until(self, condition):
        return self.wait.until(lambda _: condition())

    def drag_to(self, source, destination):
        self.driver.execute_script('arguments[0].scrollIntoView({block:"center"})', source)
        ActionChains(self.driver).click_and_hold(source).pause(0.5).move_to_element(
            destination
        ).pause(0.7).release().perform()

    def click_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR)

    def click_feed(self):
        self.click(HeaderLocators.FEED)
