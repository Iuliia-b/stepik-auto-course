from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int (x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    browser.get(link)
    browser.maximize_window()

    x_element = browser.find_element_by_xpath("//span[@id='input_value']")

    x = x_element.text
    print("x is ", x)
    y = calc(x)    

    inputField = browser.find_element_by_xpath("//input[@id='answer']")
    inputField.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    robotCheckbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    robotCheckbox.click()

    radioRobots = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radioRobots.click()

    button.click()

finally:
   
    time.sleep(5)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла