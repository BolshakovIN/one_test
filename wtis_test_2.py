from selenium import webdriver
import unittest
import time

try:
    profile = webdriver.ChromeProfile()
    profile.set_preference('network.http.phishy-userpass-length', 255)
    driver = webdriver.Firefox(C_profile=profile)
    driver.get("https://username:password@somewebsite.com/")
    link = 'http://intgr-test-1.stage.erp.vseinstrumenti.net/symfony/login'
    browser = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, options=options)
    browser.get(link)
    wait = WebDriverWait(browser, 10)
    alert = wait.until(EC.alert_is_present())
    alert = browser.switch_to(alert)
    alert.send_keys('myname')
    alert.send_keys(Keys.TAB)
    alert.send_keys('mypass')
    alert.accept()


finally:
    time.sleep(10)
    browser.quit()