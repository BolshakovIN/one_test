from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class GoogleSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.google.com/')

    def test_01(self):
        driver = self.driver
        input_field = driver.find_element_by_name('q')
        input_field.send_keys('python')
        input_field.send_keys(Keys.ENTER)

        titles = driver.find_elements_by_class_name('LC20lb DKV0Md')
        for title in titles:
            assert 'python' in title.text.lower()

    def test_02(self):
        driver = self.driver
        input_field = driver.find_element_by_name('q')
        input_field.send_keys('python')
        input_field.send_keys(Keys.DOWN)
        input_field.send_keys(Keys.DOWN)
        input_field.send_keys(Keys.ENTER)

        titles = driver.find_elements_by_class_name('LC20lb DKV0Md')
        for title in titles:
            assert 'python' in title.text.lower()

        screen = driver.get_screenshot_as_png()
        with open("screen.png", "wb") as f:
            f.write(screen)
        driver.quit()



    def tearDown(self):
        self.driver.quit()

if __name__=='__main__':
    unittest.main()