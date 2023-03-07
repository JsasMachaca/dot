
import mysql.connector
try:
    conn = mysql.connector.connect(host="localhost", user="root", password="", db="python1")
    puntero = conn.cursor()
    puntero.execute("SELECT * FROM  alumnos")
    t = puntero.fetchall()
    for i in t:
        print(i)

    conn.close()
except Exception as e:
    print(e)


