from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Настройка драйвера
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен ChromeDriver

# Открытие страницы
driver.get("http://uitestingplayground.com/classattr")

# Поиск и клик по синей кнопке
blue_button = driver.find_element(By.CLASS_NAME, "btn-primary")
blue_button.click()

# Ожидание для проверки
time.sleep(2)

# Закрыть браузер
driver.quit()