import allure

from order_helper import place_new_order
from pages.feed_page import FeedPage


@allure.feature("Лента заказов")
class TestFeed:
    @allure.title("После оформления заказа увеличивается счётчик за всё время")
    def test_total_orders_increases(self, driver, test_user, menu):
        feed = FeedPage(driver)
        feed.open("/feed")
        initial = feed.completed_all_time()
        place_new_order(driver, test_user, menu)
        feed.click_feed()
        assert feed.wait_all_time_increase(initial)

    @allure.title("После оформления заказа увеличивается счётчик за сегодня")
    def test_today_orders_increases(self, driver, test_user, menu):
        feed = FeedPage(driver)
        feed.open("/feed")
        initial = feed.completed_today()
        place_new_order(driver, test_user, menu)
        feed.click_feed()
        assert feed.wait_today_increase(initial)

    @allure.title("Номер нового заказа отображается в разделе В работе")
    def test_new_order_in_progress(self, driver, test_user, menu):
        number = place_new_order(driver, test_user, menu)
        feed = FeedPage(driver)
        feed.click_feed()
        assert feed.wait_order_in_progress(number)
