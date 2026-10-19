import os
BASE_URL = os.getenv("STELLAR_URL", "https://stellarburgers.education-services.ru").rstrip("/")
WAIT = int(os.getenv("SELENIUM_WAIT", "25"))
TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "20"))
