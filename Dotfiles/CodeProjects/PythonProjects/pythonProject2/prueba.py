import pyttsx3
import speech_recognition as rs

def cierra():
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
                print(text)
                return text
        except Exception:
            sleep(2)


cierra()