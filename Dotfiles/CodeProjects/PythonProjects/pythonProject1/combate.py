from requests_html import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep

ulr = "https://www.youtube.com"
session = HTMLSession()
r = session.get(ulr)

driver_path = "E:\\chromedriver_win32\\chromedriver.exe"
s = Service(driver_path)

driver = webdriver.Chrome(service=s)
driver.maximize_window()

driver.get(ulr)
sleep(2)

driver.find_element(By.NAME, "search_query").send_keys("hola mundo en python ")
driver.find_element(By.ID, "search-icon-legacy").click()
sleep(30)

