import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# открываем страницу
driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
driver.maximize_window()

# Находим кнопку "Add Element" и кликаем 5 раз
add_button = driver.find_element(By.XPATH, "//button[text()='Add Element']")
for _ in range(5):
    add_button.click()

# Ждем по секунде, чтобы кнопки добавились
    time.sleep(1)

# Собираем список кнопок "Delete"
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

# Выводим количество кнопок "Delete"
print("Количество кнопок Delete:", len(delete_buttons))

# Закрыть браузер
driver.quit()



