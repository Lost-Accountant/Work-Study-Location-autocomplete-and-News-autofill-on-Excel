import urllib.request
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import pandas as pd

urlpage = 'https://www.scmp.com/economy/china-economy/article/3073960/chinas-coronavirus-response-slowed-bureaucracy-unstable'

print(urlpage)

driver = webdriver.Firefox(executable_path='E:\\Geckodriver\\geckodriver.exe')

driver.get(urlpage)
driver.execute_script(
    "window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")

time.sleep(30)
