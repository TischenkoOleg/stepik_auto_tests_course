from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    time.sleep(1)
    browser.get(link)
    import math
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    
    x_element = browser.find_element(By.CSS_SELECTOR, 'img#treasure')
    x = x_element.get_attribute("valuex")
    y = calc(x)
    

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer')
    input1.send_keys(y)

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    option1.click()

    option1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    option1.click()
   

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
