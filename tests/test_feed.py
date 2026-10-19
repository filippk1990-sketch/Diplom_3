import allure

from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage
from pages.login_page import LoginPage


def place_new_order(driver, user, menu):
    LoginPage(driver).login(user)
    constructor = ConstructorPage(driver)
    constructor.add_to_basket(menu["bun"])
    constructor.add_to_basket(menu["filling"])
    number = constructor.order()
    constructor.close_order()
    return number


@allure.feature("Лента заказов")
class TestFeed:
    @allure.title("После оформления заказа увеличивается счётчик за всё время")
    def test_total_orders_increases(self, driver, test_user, menu):
        feed = FeedPage(driver)
        feed.open("/feed")
        initial = feed.completed_all_time()
        number = place_new_order(driver, test_user, menu)
        feed.click_feed()
        assert feed.wait_all_time_increase(initial)
        assert number > 0

    @allure.title("После оформления заказа увеличивается счётчик за сегодня")
    def test_today_orders_increases(self, driver, test_user, menu):
        feed = FeedPage(driver)
        feed.open("/feed")
        initial = feed.completed_today()
        number = place_new_order(driver, test_user, menu)
        feed.click_feed()
        assert feed.wait_today_increase(initial)
        assert number > 0

    @allure.title("Номер нового заказа отображается в разделе В работе")
    def test_new_order_in_progress(self, driver, test_user, menu):
        number = place_new_order(driver, test_user, menu)
        feed = FeedPage(driver)
        feed.click_feed()
        assert feed.wait_order_in_progress(number)
