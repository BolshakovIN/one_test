from selenium import webdriver
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element_by_css_selector('[name="firstname"].form-control').send_keys('Ivan')
    surname = browser.find_element_by_css_selector('[name="lastname"].form-control').send_keys('Bolshakov')
    email = browser.find_element_by_css_selector('[name="email"].form-control').send_keys('volvoman2007@mail.ru')

    current_dir = os.path.abspath(os.path.dirname('/Users/ivanbolsakov/Desktop/ ')) # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Регрессионное тестирование формы регистрации.docx')  # добавляем к этому пути имя файла
    download = browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)

    button = browser.find_element_by_css_selector('.btn.btn-primary').click()

finally:
    time.sleep(5)
    browser.quit()