import re

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import pyttsx3
import speech_recognition as rs
from time import sleep


def seguir():
    engine = pyttsx3.init()
    engine.setProperty("voice", "spanish")
    engine.say("busca otra cosa")
    engine.runAndWait()
    r = rs.Recognizer()

    with rs.Microphone() as source:
        print("escuchando")
        audio = r.listen(source)
        text = r.recognize_google(audio, language="es-ES")
        b =["Buscar ([A-Z a-z]+)", "Busca ([A-Z a-z]+)", "([A-Z a-z]+)"]
        for bs in b:
            try:
                m = re.findall(bs, text)
                print(m[0])
                return m[0]
            except Exception as e:
                print("mal")

seguir()