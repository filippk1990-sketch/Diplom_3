from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def click_constructor(self):
        self.click(HeaderLocators.CONSTRUCTOR)

    def click_feed(self):
        self.click(HeaderLocators.FEED)
