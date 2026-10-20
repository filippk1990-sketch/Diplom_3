# Diplom_3 — Stellar Burgers / UI

**Работа для сдачи:** Филипп Крощенко · когорта 53 · GitHub: [filippk1990-sketch](https://github.com/filippk1990-sketch).


Selenium 4, Page Object, pytest, Allure. Тестируются переходы, модальное окно, счётчик ингредиентов и лента заказов. Вход через UI, создание временного пользователя и удаление через API.

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pytest --browser=chrome --alluredir=allure-results/chrome
.\.venv\Scripts\python.exe -m pytest --browser=firefox --alluredir=allure-results/firefox
allure serve allure-results
```

Нужны установленные **Chrome и Firefox**; Selenium Manager автоматически получает совместимые драйверы при наличии интернета. Для видимого окна добавить `--headed`.

Переменные: `STELLAR_URL`, `SELENIUM_WAIT`, `REQUEST_TIMEOUT`. Ветка для PR: `develop3`.

Тесты ленты создают реальный заказ через UI. Глобальные счётчики могут изменяться от параллельных пользователей, поэтому проверяется увеличение, а не фиксированное значение `+1`. При ошибке скриншот помещается в Allure.


## Проверка на офлайн-симуляторе

Отчёты в папке `reports/` получены **только на локальном имитаторе**. Они не являются подтверждением поведения оригинального веб-приложения. Проверку оригинального стенда нужно запустить, когда он станет доступен.

Allure Commandline (CLI) устанавливается отдельно от Python-пакета `allure-pytest`.

Если ChromeDriver в PATH устарел, Selenium может не запуститься. Обновите ChromeDriver до основной версии установленного Chrome либо уберите старый драйвер из PATH, чтобы Selenium Manager подобрал его сам.
