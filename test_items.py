import time

from selenium.webdriver.common.by import By


def test_guest(browser):
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(5)
    assert ...