from selenium import webdriver
# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Firefox()
browser.get("https://stepik.org/lesson/25969/step/8")
browser.quit()