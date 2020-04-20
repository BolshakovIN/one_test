from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time

class VseinstrReg(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)

    def test_01(self):
        driver = self.driver
        driver.get('https://www.vseinstrumenti.ru/pcabinet/registration/')
        driver.find_element_by_id('lastName').click()
        driver.find_element_by_id('lastName').send_keys('Клоков')
        driver.find_element_by_id('firstName').click()
        driver.find_element_by_id('firstName').send_keys('Клок')
        driver.find_element_by_id('reg-phone').click()
        driver.find_element_by_id('reg-phone').send_keys('89200007888')
        driver.find_element_by_id('reg-email').click()
        driver.find_element_by_id('reg-email').send_keys('11skdfl@mail.ru')
        driver.find_element_by_id('reg-email').send_keys(Keys.ENTER)
        driver.find_element_by_id('password1').click()
        driver.find_element_by_id('password1').clear()
        driver.find_element_by_id('password1').send_keys('111111')
        driver.find_element_by_id('password2').click()
        driver.find_element_by_id('password2').clear()
        driver.find_element_by_id('password2').send_keys('111111')
        driver.find_element_by_id('reg-btn').click()


    def tearDown(self):
        self.driver.quit()
if __name__ == '_main_':
    unittest.main()