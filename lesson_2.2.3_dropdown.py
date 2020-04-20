from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select


try:
    link = 'http://suninjuly.github.io/selects1.html'
    browser = webdriver.Chrome()
    browser.get(link)

    one_number = browser.find_element_by_css_selector('.nowrap#num1')
    x = one_number.text
    two_number = browser.find_element_by_css_selector('.nowrap#num2')
    y = two_number.text
    z = str(int(x) + int(y))

    select = Select(browser.find_element_by_css_selector('#dropdown.custom-select'))
    select.select_by_value(z)
    clik_b = browser.find_element_by_css_selector('button.btn.btn-default').click()

finally:
    time.sleep(5)
    browser.quit()