import mysql.connector

conexion = mysql.connector.connect(
    host = '127.0.0.1',
    user = 'root',
    password = "23deAbril",
    database = "tienda"
)


try:
    with conexion:
        with conexion.cursor() as cursor:
            consulta = "SELECT * FROM parqueadero"
            cursor.execute(consulta)
            registros = cursor.fetchall()
            print(registros)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()