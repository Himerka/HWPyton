from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Путь к драйверу Firefox
driver = webdriver.Firefox()

try:
    # Открываем страницу
    driver.get("http://the-internet.herokuapp.com/login")

    # Ожидание для поля ввода имени пользователя с использованием id
    time.sleep(2)
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username")))
    username_field.send_keys("tomsmith")

    # Ожидание для поля ввода пароля с использованием id
    time.sleep(2)
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password")))
    password_field.send_keys("SuperSecretPassword!")

    # Ожидание для кнопки Login
    time.sleep(2)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
    login_button.click()
    time.sleep(2)

finally:
    # Закрываем браузер
    driver.quit()