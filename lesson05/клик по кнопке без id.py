import time
from selenium import webdriver
from selenium.webdriver.common.by import By


# Открываем браузер и страницу
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/dynamicid")
driver.maximize_window()

# Ждем, пока кнопка станет доступной
time.sleep(2)

# Находим синюю кнопку по классу и кликаем на нее
button = driver.find_element(By.CLASS_NAME, "btn-primary")
button.click()
time.sleep(5)

# Закрыть браузер
driver.quit()