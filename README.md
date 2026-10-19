# Diplom_3 — Stellar Burgers / UI

Selenium 4, Page Object, pytest, Allure. Тестируются переходы, модальное окно, счётчик ингредиентов и лента заказов. Вход через UI, создание временного пользователя и удаление через API.

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python -m pytest --browser=chrome --alluredir=allure-results/chrome
.venv\Scripts\python -m pytest --browser=firefox --alluredir=allure-results/firefox
allure serve allure-results
```

Нужны установленные **Chrome и Firefox**; Selenium Manager автоматически получает совместимые драйверы при наличии интернета. Для видимого окна добавить `--headed`.

Переменные: `STELLAR_URL`, `SELENIUM_WAIT`, `REQUEST_TIMEOUT`. Ветка для PR: `develop3`.

Тесты ленты создают реальный заказ через UI. Глобальные счётчики могут изменяться от параллельных пользователей, поэтому проверяется увеличение, а не фиксированное значение `+1`. При ошибке скриншот помещается в Allure.
