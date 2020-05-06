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

    def test_quest_should_login_page(self,browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")


    def test_quest_should_logout(self,browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

    # добавили маркировки для запусков тестов - xfail - заведомо падающий тест
    @pytest.mark.xfail
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("button.favorite")