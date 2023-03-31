from selenium import webdriver
from selenium.webdriver.common.by import By
import time


try:
    link = "https://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    
    x_element = browser.find_element(By.ID, 'num1')
    x = x_element.text
    y_element = browser.find_element(By.ID, 'num2')
    y = y_element.text
    s = (int(x)+int(y))
    
    from selenium.webdriver.support.ui import Select
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(str(s)) # ищем сумму

    option1 = browser.find_element(By.CSS_SELECTOR, "button.btn")
    option1.click()
   

    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

   # не забываем оставить пустую строку в конце файла 
