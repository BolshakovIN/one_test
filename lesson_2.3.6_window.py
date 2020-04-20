from selenium import webdriver
import time
import math
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser = webdriver.Chrome()
    browser.implicitly_wait(5)
    browser.get(link)

    browser.find_element_by_css_selector('[type="submit"].trollface.btn.btn-primary').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    num = browser.find_element_by_css_selector('.nowrap#input_value')
    x = num.text
    y = calc(x)
    field = browser.find_element_by_css_selector('.form-control#answer')
    field.send_keys(y)

    submit_ok = browser.find_element_by_css_selector('[type="submit"].btn.btn-primary')
    submit_ok.click()

finally:
    browser.quit()