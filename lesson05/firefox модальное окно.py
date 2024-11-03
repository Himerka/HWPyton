from sys import executable

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

# Открываем страницу
driver.get("http://the-internet.herokuapp.com/entry_ad")

# Ждем загрузки модального окна
time.sleep(2)

# Нажимаем на кнопку Close
close_button = driver.find_element(By.CSS_SELECTOR, ".modal-footer > p:nth-child(1)")
close_button.click()

# Пауза для наблюдения результата
time.sleep(2)

# Закрываем браузер
driver.quit()