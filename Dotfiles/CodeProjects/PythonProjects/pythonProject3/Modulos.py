import pymysql as mysql


# Módulo de conexión a una base de datos mysql
def connection(host, user, password, database):
    con = mysql.Connection(host=host, user=user, password=password, database=database)
    cursor = con.cursor()
    cursor.execute("insert into cuentas values ('jessss', 'jeeee')")
    con.commit()


def connection_(host, user, password, database):
    con = mysql.Connection(host=host, user=user, password=password, database=database)
    return con


# Función para ejecutar una consulta
def execution_query(cursor, query):
    cursor.execute(query)
    print(cursor.fetchall())


def executions(con, cursor, query):
    cursor.execute(query)
    con.commit()
    con.close()


connection("localhost", "root", "godylody31", "accounts")

