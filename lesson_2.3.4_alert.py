from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    submit = browser.find_element_by_css_selector('.btn.btn-primary').click()
    confirm = browser.switch_to.alert
    confirm.accept()

    num = browser.find_element_by_css_selector('.nowrap#input_value')
    x = num.text
    y = calc(x)
    field = browser.find_element_by_css_selector('.form-control#answer')
    field.send_keys(y)

    submit_ok = browser.find_element_by_css_selector('[type="submit"].btn.btn-primary')
    submit_ok.click()

finally:
    time.sleep(5)
    browser.quit()