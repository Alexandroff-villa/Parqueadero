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
            consulta = "SELECT * FROM parqueadero WHERE id IN (%s)"
            entrada = input("Proporcione los id's a buscar (separado por comas): ").split(",")
            llaves_primarias = ','.join(list(map(lambda arg: "'%s'" % arg, entrada)))
            consulta = consulta % llaves_primarias
            cursor.execute(consulta)
            registros = cursor.fetchall()
            for registro in registros:
                print(registro)

except Exception as e:
    print(f'Ocurrio un error: {e}')
finally:
    conexion.close()