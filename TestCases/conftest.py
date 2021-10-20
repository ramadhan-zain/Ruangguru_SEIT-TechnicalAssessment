import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = None


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome(executable_path="./assets/drivers/chromedriver.exe")
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path="./assets/drivers/geckodriver.exe.exe")

    driver.get("https://skillacademy.com/")
    driver.maximize_window()

    wait = WebDriverWait(driver, 7)

    request.cls.driver = driver
    request.cls.wait = wait
    yield

    time.sleep(1)
    driver.close()



