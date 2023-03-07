import pyttsx3
import speech_recognition as rs

engine = pyttsx3.init()
engine.setProperty("voice", "spanish")
engine.say("hola, ¿Cómo estás?, cual es tu nombre")
engine.runAndWait()
r = rs.Recognizer()

with rs.Microphone() as source:
    print("dime tu nombre")
    audio = r.listen(source)
    text = r.recognize_google(audio, language="es-ES")
    engine.say("mucho gusto"+text)
    engine.runAndWait()

