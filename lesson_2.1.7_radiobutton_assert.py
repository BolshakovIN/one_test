from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/get_attribute.html'
    browser = webdriver.Chrome()
    browser.get(link)

    x_element = browser.find_element_by_css_selector("img#treasure[valuex]")
    x = x_element.get_attribute('valuex')
    y = calc(x)
    find_field = browser.find_element_by_css_selector('#answer[type="text"]')
    find_field.send_keys(y)
    find_checkbox = browser.find_element_by_css_selector('input.check-input[type="checkbox"]')
    find_checkbox.click()
    find_radiobutton = browser.find_element_by_css_selector('input.check-input[type="radio"]#robotsRule')
    find_radiobutton.click()
    butoon_checked = find_radiobutton.get_attribute('value')
    assert butoon_checked == "robots"
    find_submit = browser.find_element_by_css_selector('button.btn.btn-default')
    find_submit.click()

finally:
    time.sleep(5)
    browser.quit()
