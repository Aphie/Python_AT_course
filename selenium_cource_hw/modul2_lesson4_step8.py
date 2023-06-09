from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome('C:\\Users\\s.andreyuk\\selenium_cource\\chromedriver_win32\\chromedriver.exe')
    browser.get(link)
    
    # отправляем форму
    button = browser.find_element(By.ID, "book")
    WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100"))
    
    button.click()
    
    # берем значение числа, вычисляем, вводим данные в поле и отправляем 
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)
    answer_field = browser.find_element(By.ID, "answer")
    answer_field.send_keys(y)
    
    button2 = browser.find_element(By.ID, "solve")
    button2.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()