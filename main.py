from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
import datetime
from selenium.webdriver.support.ui import Select
#chromium.exe path
driver = webdriver.Chrome(executable_path="C://chromedriver.exe")
driver.maximize_window()
#url of website
driver.get('file:///D:/Portfolio/PORTFOLIO%20WEB/portfolio.html')
#stays for page till 10 seconds
driver.implicitly_wait(10)
#navigating pages

sleep(10)
driver.close()