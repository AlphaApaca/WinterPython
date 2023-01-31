import time
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service

wd = webdriver.Chrome()
# wd = webdriver.Chrome(service=Service(r'd:\tools\chromedriver.exe'))
wd.get('https://www.baidu.com')

input()
# time.sleep(100000)