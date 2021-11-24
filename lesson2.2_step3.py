from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    browser.get(link)
    browser.maximize_window()

    x_element = browser.find_element_by_xpath("//span[@id='num1']")
    x = x_element.text
    print("x is ", x)

    y_element = browser.find_element_by_xpath("//span[@id='num2']")
    y = y_element.text
    print("y is ", y)

    sum = str(int(x)+int(y))

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(sum) 

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
   
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла