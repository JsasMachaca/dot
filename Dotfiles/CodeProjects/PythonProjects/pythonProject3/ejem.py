import pymysql


# función que retorna objeto tipo cursor
def connection():
    try:
        con = pymysql.connect(user='root', password='godylody31', db='accounts')
        cursor = con.cursor()
        return cursor
    except Exception as ex:
        print("Error al conectar a la base de datos.\n")
        print('\t', ex)


# función que almacena un cursor y devuelve una query
def execute_query(cursor, ext_query):
    try:
        cursor.execute(ext_query)
        selct = cursor.fetchall()
        if selct:
            for i in selct:
                for n in i:
                    print("Datos encontrados: ", n)
            return selct
        else:
            print("No se encuentran esos datos")
    except Exception as exp:
        print("Ocurrió un error: ", exp)


# función lambda que almacena una sentancia a ejecutar
val_sentence = lambda user, passwd: f"select * from cuentas where usuarios = '{user}' and contraseñas = '{passwd}';"


# función que almacena un procedimiento dado después de validar el nombre y la contraseña
def pr(n):
    if n:
        print("hola mundo xdxdxdxx")
    else:
        print("prueba otra vez")


# función principal
def main():
    user = input("Nombre de usuario: ")
    passwd = input("Contraseña: ")
    f = val_sentence(user, passwd)  # creando una sentencia con los datos pedidos
    cursor = connection()  # conexión con la base de datos que devuelve un cursor
    l = execute_query(cursor, f)  # ejecución de la sentencia creada (f)
    pr(l)  # ejecutando función después de la validación


if __name__ == "__main__":
    main()
