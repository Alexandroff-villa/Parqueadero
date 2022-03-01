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
            sentencia = 'UPDATE parqueadero SET marca=%s WHERE id=%s'
            valores = ("Toyota", 5)
            cursor.execute(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()