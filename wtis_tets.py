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
        driver.get('http://intgr-test-1.stage.erp.vseinstrumenti.net/symfony/login')
        driver.find_element_by_name('_username').click()
        driver.find_element_by_name('_username').send_keys('BolshakovIN')
        driver.find_element_by_name('_password').click()
        driver.find_element_by_name('_password').send_keys('Ba09012025')
        driver.find_element_by_name('_password').send_keys(Keys.ENTER)
        driver.get('http://intgr-test-1.stage.erp.vseinstrumenti.net/symfony/?redirect=/docs/Zayavka_List/doc_zayavki/')
        driver.find_element_by_css_selector('/img/ico/20.gif').click()
        driver.find_element_by_css_selector('/img/ico/20.gif').click()

    def tearDown(self):
        self.driver.quit()
if __name__ == '_main_':
    unittest.main()