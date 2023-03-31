from selenium import webdriver
from selenium.webdriver.common.by import By
import time


link = "https://SunInJuly.github.io/execute_script.html"

try:
       
    browser = webdriver.Chrome()
    time.sleep(1)
    browser.get(link)
    
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    x = browser.find_element(By.CSS_SELECTOR, '#input_value').text
    y = calc(x)
    

    input1 = browser.find_element(By.CSS_SELECTOR, '#answer.form-control').send_keys(y)
    
    button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()

    browser.find_element(By.CSS_SELECTOR, "#robotsRule").click()

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    
    
    
finally:
 # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла



