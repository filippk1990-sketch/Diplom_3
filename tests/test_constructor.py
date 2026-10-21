import allure
from pages.constructor_page import ConstructorPage
from pages.feed_page import FeedPage


@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("Переход в Конструктор по ссылке")
    def test_go_to_constructor(self, driver):
        feed = FeedPage(driver)
        feed.open("/feed")
        feed.click_constructor()
        assert ConstructorPage(driver).is_open()

    @allure.title("Переход в Ленту заказов по ссылке")
    def test_go_to_feed(self, driver):
        constructor = ConstructorPage(driver)
        constructor.open()
        constructor.click_feed()
        assert FeedPage(driver).is_open()

    @allure.title("По клику на ингредиент открываются детали")
    def test_ingredient_details_open(self, driver):
        page = ConstructorPage(driver)
        page.open()
        title = page.open_ingredient_details()
        assert title == "Детали ингредиента"
        assert page.is_details_modal_open()

    @allure.title("Крестик закрывает окно деталей")
    def test_details_close(self, driver):
        page = ConstructorPage(driver)
        page.open()
        page.open_ingredient_details()
        page.close_modal()
        assert page.is_details_modal_closed()

    @allure.title("После перетаскивания счётчик ингредиента увеличивается")
    def test_ingredient_counter(self, driver, menu):
        page = ConstructorPage(driver)
        page.open()
        before = page.ingredient_count(menu["filling"])
        page.add_to_basket(menu["filling"])
        assert page.wait_ingredient_count(menu["filling"], before + 1)
