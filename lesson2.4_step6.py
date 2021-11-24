from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int (x)))))

try: 
    link = "http://suninjuly.github.io/cats.html"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    browser.get(link)
    browser.maximize_window()
    
    button = browser.find_element_by_id("button")
    button.click()
    
finally:
   
    time.sleep(5)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла