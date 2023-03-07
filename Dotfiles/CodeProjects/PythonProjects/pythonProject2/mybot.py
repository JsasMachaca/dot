import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pyttsx3
import speech_recognition as rs
from time import sleep


def dormir():
    sleep(3)


def service():
    return Service()


def voice_tittle():
    while True:
        try:
            engine = pyttsx3.init()
            engine.setProperty("voice", "spanish")
            engine.say("hola, ¿qué quieres buscar?")
            engine.runAndWait()
            r = rs.Recognizer()
            with rs.Microphone() as source:
                print("escuchando")
                audio = r.listen(source)
                text = r.recognize_google(audio, language="es-ES")
                t = ["Busca ([A-Z a-z]+)", "Buscar ([A-Z a-z]+)", "([A-Z a-z]+)"]
                for ts in t:
                    try:
                        m = re.findall(ts, text)
                        print(m[0])
                    except IndexError:
                        pass
                return m[0]
        except Exception:
            pass



def chrome_driver_init(ulr, servicios):
    driver = webdriver.Chrome(service=servicios)
    driver.maximize_window()
    driver.get(ulr)
    return driver



def chrome_finder(driver, titulo):
    driver.find_element(By.NAME, "search_query").send_keys(titulo)
    dormir()
    driver.find_element(By.ID, "search-icon-legacy").click()
    dormir()
    driver.find_element(By.CLASS_NAME, "yt-simple-endpoint style-scope ytd-video-renderer".replace(" ", ".")).click()



def exit_confirmation():
    while True:
        try:
            engine = pyttsx3.init()
            engine.setProperty("voice", "spanish")
            engine.say("quieres salir?")
            engine.runAndWait()
            r = rs.Recognizer()
            with rs.Microphone() as source:
                print("escuchando")
                audio = r.listen(source)
                text = r.recognize_google(audio, language="es-ES")
                return text
        except Exception:
            sleep(2)



def main():
    ulr = "https://www.youtube.com/"
    s = service()
    n = voice_tittle()
    sleep(5)
    b = chrome_driver_init(ulr, s)
    chrome_finder(b, n)
    sleep(10)
    cerrar = exit_confirmation()
    while True:
        if cerrar == "salir" or cerrar == "sí":
            break
        else:
            sleep(300)


if __name__ == "__main__":
    main()
