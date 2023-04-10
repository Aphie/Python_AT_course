from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome('C:\\Users\\s.andreyuk\\selenium_cource\\chromedriver_win32\\chromedriver.exe')
    browser.get(link)
    
    # отправляем форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()
    
    # обрабатываем alert
    confirm = browser.switch_to.alert
    confirm.accept()
    
    # берем значение числа, вычисляем, вводим данные в поле и отправляем 
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    button2 = browser.find_element(By.TAG_NAME, "button")
    button2.click()
    
    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()