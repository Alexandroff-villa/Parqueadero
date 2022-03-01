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
            sentencia = 'INSERT INTO parqueadero(placa,marca,color,fecha) VALUES (%s, %s, %s, %s);'
            valores = (
                ("EEE-123","Nissan","fuccia","01/03/2022"),
                ("FFF-123","Hiunday","rojo","01/03/2022"),
                ("GGG-123","Wolsvaguen","negro","01/03/2022")
                )
            cursor.executemany(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()