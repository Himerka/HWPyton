from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Путь к драйверу Firefox
driver = webdriver.Firefox()

try:
    # Шаг 1: Открыть страницу
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Шаг 2: Найти поле ввода и ввести 1000
    input_field = driver.find_element(By.XPATH, "//input[@type='number']")
    time.sleep(2)
    input_field.send_keys("1000")
    time.sleep(2)

    # Шаг 3: Очистить поле ввода
    input_field.clear()
    time.sleep(2)


    # Шаг 4: Ввести текст 999
    input_field.send_keys("999")


    # Задержка для наблюдения за результатом
    time.sleep(3)

finally:
    # Закрыть браузер
    driver.quit()