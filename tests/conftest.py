import uuid

import allure
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

from config import BASE_URL, TIMEOUT


def pytest_addoption(parser):
    parser.addoption("--browser", choices=["chrome", "firefox"], default="chrome",
                     help="Browser for Selenium UI tests")
    parser.addoption("--headed", action="store_true", help="Display the browser window")


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    options = ChromeOptions() if browser == "chrome" else FirefoxOptions()
    if not request.config.getoption("--headed"):
        options.add_argument("--headless=new" if browser == "chrome" else "-headless")
    if browser == "chrome":
        options.add_argument("--window-size=1440,1000")
    instance = webdriver.Chrome(options=options) if browser == "chrome" else webdriver.Firefox(options=options)
    instance.set_window_size(1440, 1000)
    instance.set_page_load_timeout(45)
    try:
        yield instance
    finally:
        try:
            if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
                allure.attach(instance.get_screenshot_as_png(), name="screenshot_on_failure",
                              attachment_type=allure.attachment_type.PNG)
        finally:
            instance.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    setattr(item, "rep_" + outcome.get_result().when, outcome.get_result())


@pytest.fixture
def api():
    with requests.Session() as session:
        yield session


@pytest.fixture
def test_user(api):
    """Fixture prepares user and cleans up; it does not check responses."""
    value = uuid.uuid4().hex
    user = {"email": f"ui.{value}@example.com", "password": f"Qa-{value}",
            "name": f"UI-{value[:7]}"}
    response = api.post(f"{BASE_URL}/api/auth/register", json=user, timeout=TIMEOUT)
    token = response.json()["accessToken"]
    try:
        yield user
    finally:
        api.delete(f"{BASE_URL}/api/auth/user",
                   headers={"Authorization": token}, timeout=TIMEOUT)


@pytest.fixture
def menu(api):
    """Prepare dynamic ingredient labels without performing test assertions."""
    data = api.get(f"{BASE_URL}/api/ingredients", timeout=TIMEOUT).json()["data"]
    bun = next(item for item in data if item["type"] == "bun")
    filling = next(item for item in data if item["type"] != "bun")
    return {"bun": bun["name"], "filling": filling["name"]}
