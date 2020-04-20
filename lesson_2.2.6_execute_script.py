from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)
    elem = browser.find_element_by_css_selector('.nowrap#input_value')
    x = elem.text
    y = calc(x)
    field = browser.find_element_by_css_selector('#answer[class="form-control"]')
    field.send_keys(y)
    button = browser.find_element_by_css_selector('.btn.btn-primary')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    check = browser.find_element_by_css_selector('.form-check-input[type="checkbox"]').click()
    radio = browser.find_element_by_css_selector('.form-check-input[name="ruler"]#robotsRule').click()
    button.click()

finally:
    time.sleep(5)
    browser.quit()