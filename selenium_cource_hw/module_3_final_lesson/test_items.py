import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_buy_button_available(browser):
    link =  " http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(2)
    assert len(browser.find_elements(By.CLASS_NAME, "btn-add-to-basket")) > 0, "no such element on the page"