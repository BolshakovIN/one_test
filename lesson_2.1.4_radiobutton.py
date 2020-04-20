from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector('.nowrap#input_value')
    x = x_element.text
    y = calc(x)
    find_field = browser.find_element_by_css_selector('#answer.form-control[type="text"]')
    find_field.send_keys(y)
    find_checkbox = browser.find_element_by_id("robotCheckbox")
    find_checkbox.click()
    find_radiobutton = browser.find_element_by_css_selector(".form-check-input#robotsRule")
    find_radiobutton.click()
    find_submit = browser.find_element_by_css_selector('button.btn.btn-default')
    find_submit.click()

finally:
    time.sleep(10)
    browser.quit()


