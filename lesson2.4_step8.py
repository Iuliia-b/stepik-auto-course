from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int (x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    browser.get(link)
    browser.maximize_window()
    
    button = browser.find_element_by_xpath("//button[@id='book']")
    
    WebDriverWait(browser, 20).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    
    button.click()
    
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")

    x = x_element.text
    print("x is ", x)
    y = calc(x)    

    inputField = browser.find_element_by_xpath("//input[@id='answer']")
    inputField.send_keys(y)
    
    submit = browser.find_element_by_xpath("//button[@id='solve']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()   
    
finally:
   
    time.sleep(5)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла