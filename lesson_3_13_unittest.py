from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class NewTestUnittest(unittest.TestCase):

    def test_01(self):
        link = 'http://suninjuly.github.io/registration1.html'
        self.driver = webdriver.Chrome()
        self.driver.get(link)
        browser = self.driver
        browser.implicitly_wait(5)
        input1 = browser.find_element_by_css_selector('.first_class .first:nth-child(2)[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            '.second_class .second:nth-child(2)[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.third[placeholder="Input your email"]')
        input3.send_keys("lala@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)

    def test_02(self):
        link_02 = 'http://suninjuly.github.io/registration2.html'
        self.driver = webdriver.Chrome()
        self.driver.get(link_02)
        browser = self.driver
        browser.implicitly_wait(5)
        input1 = browser.find_element_by_css_selector('.first_class .first:nth-child(2)[placeholder="Input your first name"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(
            '.second_class .second:nth-child(2)[placeholder="Input your last name"]')
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector('.third[placeholder="Input your email"]')
        input3.send_keys("lala@mail.ru")
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        welcome_text_elt = browser.find_element_by_tag_name("h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()
