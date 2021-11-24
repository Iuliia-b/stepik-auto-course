from selenium import webdriver
import time
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/math.html"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    browser.get(link)
    browser.maximize_window()

    people_radio = browser.find_element_by_id("peopleRule")

    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)

    assert people_checked is not None, "People radio is not selected by default"

    robots_radio = browser.find_element_by_id("robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    assert robots_checked is None

  # x_element = browser.find_element_by_id('input_value')
    x_element = browser.find_element_by_xpath("//span[@id='input_value']")
  # x_element = browser.find_element_by_css_selector('#input_value')

    x = x_element.text
    y = calc(x)    

    inputField = browser.find_element_by_xpath("//input[@id='answer']")
    inputField.send_keys(y)

    robotCheckbox = browser.find_element_by_xpath("//input[@id='robotCheckbox']")
    robotCheckbox.click()

    radioRobots = browser.find_element_by_xpath("//input[@id='robotsRule']")
    radioRobots.click()

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
   
    time.sleep(5)
    browser.quit()

# не забываем оставить пустую строку в конце файла