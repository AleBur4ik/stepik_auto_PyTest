import time
from selenium.webdriver.common.by import By


def test_button(browser):
    browser.implicitly_wait(10)
    link = f"https://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(4)
    assert browser.find_elements(By.CLASS_NAME,
                                 'btn-add-to-basket'), 'нет кнопки "Добавить в корзину"'
