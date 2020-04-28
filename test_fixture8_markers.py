from selenium import webdriver
import pytest

link = 'http://selenium1py.pythonanywhere.com/'

@pytest.fixture
def browser():
    print('\nstart open browser')
    browser = webdriver.Chrome()
    yield browser
    print('\nquit browser quit')
    browser.quit()

class TestMainPage():
    #добавили маркировки для запусков тестов
    @pytest.mark.smoke
    def test_quest_should_login_page(self,browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    @pytest.mark.win10
    def test_quest_should_logout(self,browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")