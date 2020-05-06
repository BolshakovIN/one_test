from selenium import webdriver
import pytest

@pytest.fixture(scope='function')
def browser():
    print('\ntest start browser for test')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser, finish case')
    browser.quit()