from logger import log
import mysql.connector

from usuario import Usuario 


class UsuarioDAO:
    '''
    DAO (Data Access Objetc)
    CRUD (Create-Read-Update-Delete)
    '''

    def __init__(self):
        try:
            self.conexion = mysql.connector.connect(
                host = "localhost",
                user = "root",
                password = "23deAbril",
                port = 3306,
                db = "tienda"
                )
        except Exception as e:
            print(f'Error no se pudo realozar la conexion: {e}')



        self.SELECCIONAR = 'SELECT * FROM parqueadero ORDER BY id'
        self.INSERTAR = "INSERT INTO parqueadero(placa,marca,color,fecha) VALUES (%s, %s, %s, %s)"

    def seleccionar(self):
        if self.conexion.is_connected():
            try: 
                cursor = self.conexion.cursor()
                cursor.execute(self.SELECCIONAR)
                registros = cursor.fetchall()
                Usuarios = []
                for registro in registros:
                    usuario = Usuario(registro[0],registro[1],registro[2],registro[3],registro[4])
                    Usuarios.append(usuario)
                return Usuarios
            except Exception as e:
                print(f'Ocurrio un error al seleccionar: {e}')

    def insertar(self,usuario):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                values = (usuario.placa,usuario.marca,usuario.color,usuario.fecha)
                cursor.execute(self.INSERTAR,values)
                self.conexion.commit()
            except Exception as e:
                print(f'Ocurrio un error al inertar un usuario: {e}')

if __name__ == '__main__':
    #insertar objeto
    # usuario1 = Usuario(placa="JJJ-123",marca="Hino",color="verde",fecha="02/03/2022")
    # usuarios_insertados = UsuarioDAO().insertar(usuario1)

    #Seleccionar objetos
    usuarios = UsuarioDAO().seleccionar()
    for usuario in usuarios:
        log.debug(usuario)