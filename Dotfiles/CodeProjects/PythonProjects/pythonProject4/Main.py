from time import sleep

from selenium import webdriver
from requests_html import HTMLSession
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

ulr = "https://www.amazon.com/SteelSeries-videojuegos-iluminaci%C3%B3n-PrismSync-programables" \
      "/dp/B093LSMKL3/ref=sr_1_2_sspa?keywords=gaming%2Bmouse&pd_rd_r=2db0b941-0334-47a6-aa60" \
      "-d6d46038e065&pd_rd_w=WZOzR&pd_rd_wg=7vzRF&pf_rd_p=8148f1e1-83ed-498f-85be-ff288b197da" \
      "7&pf_rd_r=ETZM6EKQ7VTR8CC3PWF3&qid=1674427315&sr=8-2-spons&spLa=ZW5jcnlwdGVkUXVhbGlmaW" \
      "VyPUEyTFdCOEZPNUFBSlpTJmVuY3J5cHRlZElkPUEwOTgwNDg3MjBZMlkzNTZBWkpFQiZlbmNyeXB0ZWRBZElk" \
      "PUEwMjYyNDcwWE5OQ1hYU09JUDVDJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ&th=1"
while True:
    try:
        session = HTMLSession()
        a = session.get(ulr)
        z = a.html.find("#buyNow_feature_div")
        print(z)
        if len(z) > 0:

            print("Se puede comprar man!!!!!!!")
            driver = webdriver.Chrome(service=Service())
            driver.maximize_window()
            driver.get(ulr)
            driver.find_element(By.ID, "buyNow_feature_div").click()
            break
        else:
            print("no se puede comprar")
            sleep(0)
    except Exception as exp:
        print("ocurrió un error xd")
        print(exp)
