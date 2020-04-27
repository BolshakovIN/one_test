from selenium import webdriver
import time
import math
import pytest

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
link = "http://suninjuly.github.io/math.html"

@pytest.fixture(scope='class')
def browser():
    print('\ntest browser for test...')
    browser = webdriver.Chrome()
    yield browser
    print('\ntest browser...')
    browser.quit()

class TestRadioButton():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_assert_radiobutton(self, browser):
        print('start test')
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
        print('finish test')



