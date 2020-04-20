from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
        link = 'http://intgr-test-1.stage.erp.vseinstrumenti.net/symfony/login'
        browser = webdriver.Chrome()
        browser.implicitly_wait(10)
        browser.get(link)
#логин
        name = browser.find_element_by_css_selector('.form-control[name="_username"]').click()
        name_input = browser.find_element_by_css_selector('.form-control[name="_username"]').send_keys('BolshakovIN')
        surname = browser.find_element_by_css_selector('.form-control[name="_password"]').click()
        surname_input = browser.find_element_by_css_selector('.form-control[name="_password"]').send_keys('Ba09012025')
        submit = browser.find_element_by_css_selector('.btn.btn-vi.login-button').click()

#Переход Журнал заказов
        zhurnal = browser.find_element_by_xpath('//a[text()="Журналы "]').click()
        zakaz = browser.find_element_by_css_selector('#mainMenuNav > li.open > ul > li:nth-child(2)').click()
        zayvka = browser.find_element_by_css_selector('#mainMenuNav > li.open > ul > li:nth-child(2) > ul > li:nth-child(5) > a').click()

#переключаемся на основной фрейм
        iframe = browser.find_element_by_xpath("//iframe[@name='mainWindow']")
        browser.switch_to.frame(iframe)

#Кликаем на предупреждение
        warning = browser.find_element_by_css_selector('[type="button"]#errorBtn').click()

#Новый заказ
        new_zayvka = browser.find_element_by_xpath('//*[@id="filterForm"]/table/tbody/tr[1]/td[1]/table/tbody/tr[1]/td[1]/img').click()
#Получаем список вкалдок и переключаемся на новую вкалдку
        new_window = browser.window_handles[1]
        browser.switch_to.window(new_window)
#Кликаем ок по аллерту
        alert_01 = browser.switch_to.alert
        alert_01.accept()
#Выбор доставки
        #time.sleep(5)
        select = Select(browser.find_element_by_css_selector('  .input3#deliver_to'))
        select.select_by_value("В офис")
        alert_02 = browser.switch_to.alert
        alert_02.accept()
#Добавляем КЛ по №телефона
        number_tel = browser.find_element_by_css_selector("#newContFacePhone").click()
        number_tel_past = browser.find_element_by_css_selector("#newContFacePhone").send_keys("9200666599")
        body = browser.find_element_by_css_selector('.readonly-backlight#number').click()
        browser.waitForElementVisible('#searchContractorByContactsModal')
        radio = browser.find_element_by_css_selector('[align="center"]>td>[name="kontrSelected"]').click()
        ok_kontr = browser.find_element_by_css_selector('#chooseFoundContractorButton').click()
#Сохраняем заказ и добавим товар
        save_button = browser.find_element_by_css_selector('#save_button')
        save_button.click()
        nomenkl = browser.find_element_by_css_selector('#addNomenclatureBtn').click()
       #new_window_01 = browser.window_handles(2)
        browser.switch_to.window('nomenkl')
        time.sleep(3)
        goods = browser.find_element_by_css_selector('#nom_id').send_keys('5195')
        find = browser.find_element_by_css_selector('[type="submit"].input3').click()
        browser.switch_to.frame('searchResults')
      #  button = WebDriverWait(browser, 5).until(
       #         EC.element_to_be_clickable((By.CSS_SELECTOR, '#cell_0_22 > input'))
      #  )
       # button.click()
        time.sleep(3)
        add = browser.find_element_by_css_selector('[value="Добавить"]').click()
        browser.close()
finally:
    time.sleep(10)
    browser.quit()