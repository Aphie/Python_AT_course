from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome('C:\\Users\\s.andreyuk\\selenium_cource\\chromedriver_win32\\chromedriver.exe')
    browser.get(link)

    # заполняем данные формы
    name = browser.find_element(By.NAME, "firstname")
    name.send_keys("Ivan")
    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Ivanov")
    email = browser.find_element(By.NAME, "email")
    email.send_keys("smolensk@email.ci")
    
    # вводим поле
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла 
    file = browser.find_element(By.ID, "file")
    file.send_keys(file_path)
    
    # отправляем форму
    button = browser.find_element(By.TAG_NAME, "button")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()