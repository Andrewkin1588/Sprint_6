import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    driver = webdriver.Firefox()
    return driver


def teardown_browser(browser):
    return browser.quit()
