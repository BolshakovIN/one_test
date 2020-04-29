from selenium import webdriver
import pytest
import time
import math

@pytest.fixture(scope='function')
def browser():
    print('\ntest run')
    browser=webdriver.Chrome()
    yield browser
    print('\ntest finished')
    browser.quit()

#задаем параметры для теста, менякется только часть урла
@pytest.mark.parametrize('url_number', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_assert_text_correct(browser, url_number):
    link = f'https://stepik.org/lesson/{url_number}/step/1'
    answer = math.log(int(time.time()))
    browser.get(link)
    browser.implicitly_wait(10)
    input_field = browser.find_element_by_css_selector('.textarea')
    a = str(answer)
    input_field.send_keys(a)
    submit = browser.find_element_by_css_selector('.submit-submission').click()
    assert_field = browser.find_element_by_css_selector('.smart-hints__hint')
    correct = assert_field.text
    assert correct =='Correct!',\
        "Don't correct resault"