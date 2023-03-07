from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from time import sleep
import pyttsx3
import speech_recognition as rs


def dormir():
    sleep(3)


def servicio():
    return Service()


def buscar(titulo, ulr, servicios):
    driver = webdriver.Chrome(service=servicios)
    driver.maximize_window()
    driver.get(ulr)
    driver.find_element(By.NAME, "search_query").send_keys(titulo)
    dormir()
    driver.find_element(By.ID, "search-icon-legacy").click()
    dormir()
    driver.find_element(By.CLASS_NAME, "yt-simple-endpoint style-scope ytd-video-renderer".replace(" ", ".")).click()
    sleep(300)

"""
def voice():
    engine = pyttsx3.init()
    engine.setProperty("voice", "spanish")
    engine.say("Hola mi amor, te dedico esta canción.")
    engine.runAndWait()
    r = rs.Recognizer()
"""

def main():
    ulr = "https://www.youtube.com/"
    driver_path = ""
    s = servicio()
    buscar("Te quiero josé luis perales", ulr, s)
    sleep(320)


if __name__ == "__main__":
    main()
