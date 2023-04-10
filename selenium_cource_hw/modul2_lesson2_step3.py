from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

import math

try: 
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome('C:\\Users\\s.andreyuk\\selenium_cource\\chromedriver_win32\\chromedriver.exe')
    browser.get(link)

    # получаем значение переменных
    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    
    # выбирает значение в выпадающем списке и кликаем на кнопку
    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(int(x)+int(y)))
    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()