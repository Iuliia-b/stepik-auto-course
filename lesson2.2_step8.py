from selenium import webdriver
import os
import time

try: 
    link = "http://suninjuly.github.io/file_input.html"

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    
    browser.get(link)
    browser.maximize_window()

    firstName = browser.find_element_by_name("firstname")
    firstName.send_keys("Taddy")

    lastName = browser.find_element_by_name("lastname")  
    lastName.send_keys("Bear")  

    email = browser.find_element_by_name("email")
    email.send_keys("toys@gmail.ru") 

    element = browser.find_element_by_xpath("//input[@id='file']")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))         # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'sample.txt')              # добавляем к этому пути имя файла 
    element.send_keys(file_path)    
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
   
    time.sleep(5)
    browser.quit()
    
# не забываем оставить пустую строку в конце файла