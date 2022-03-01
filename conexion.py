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
            valores = ("DDD-123","Nissan","plateado","01/03/2022")
            cursor.execute(sentencia, valores)
            conexion.commit()
            registros_insertados = cursor.rowcount
            print(f'Registros insertados: {registros_insertados}')

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()