from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int (x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    browser.get(link)
    browser.maximize_window()
    
    buttonWish = browser.find_element_by_xpath("//button")
    buttonWish.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")

    x = x_element.text
    print("x is ", x)
    y = calc(x)    

    inputField = browser.find_element_by_xpath("//input[@id='answer']")
    inputField.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
   
    time.sleep(5)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла