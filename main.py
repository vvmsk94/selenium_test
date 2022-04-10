from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import os
import math
import random

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser.get(link)

    input1=browser.find_element_by_css_selector(".btn")
    input1.click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
   
    x_el = browser.find_element_by_css_selector("[id='input_value']")
    x=x_el.text
    y=str(math.log(abs(12*math.sin(int(x)))))
    input2 = browser.find_element_by_css_selector("[id='answer']")
    input2.send_keys(y)
  
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:

    time.sleep(10)

    browser.quit()

