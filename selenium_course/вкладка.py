from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
link = "http://suninjuly.github.io/redirect_accept.html"

try:
    browser = webdriver.Chrome()
    time.sleep(1)
    browser.get(link)
    # Нажать на кнопку
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
    # Переключиться на новую вкладку
    browser.switch_to.window(browser.window_handles[1])
    # Посчитать математическую функцию от x
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)
    # Ввести ответ в текстовое поле
    input1 = browser.find_element(By.CSS_SELECTOR, '#answer.form-control').send_keys(y)
    # Нажать на кнопку Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
finally:
    # ожидание чтобы визуально оценить результаты
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
