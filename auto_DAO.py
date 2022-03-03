from conexion import Conexion
from usuario import Usuario
from logger import log


class UsuarioDAO:
    '''
    DAO (Data Access Objetc)
    CRUD (Create-Read-Update-Delete)
    '''

    _SELECCIONAR = 'SELECT * FROM parqueadero ORDER BY id'
    _INSERTAR = 'INSERT INTO parqueadero(placa,marca,color,fecha) VALUES(%s, %s, %s,%s)'
    _ACTUALIZAR = 'UPDATE parqueadero SET placa=%s, marca=%s, color=%s WHERE id=%s'
    _ELIMINAR = 'DELETE FROM parqueadero WHERE id=%s'

    @classmethod
    def seleccionar(cls):
        with Conexion.obtenerCursor() as cursor:
            cursor.execute(cls._SELECCIONAR)
            registros = cursor.fetchall()
            Usuarios = []
            for registro in registros:
                usuario = Usuario(registro[0],registro[1],registro[2],registro[3],registro[4])
                Usuarios.append(usuario)
            return Usuarios

    @classmethod
    def insertar(cls,usuario):
        with Conexion.obtenerConexion() as conexion:
            with conexion.cursor() as cursor:
                valores = (usuario.placa, usuario.marca, usuario.color, usuario.fecha)
                cursor.execute(cls._INSERTAR, valores)
                log.debug(f'persona a insetar: {usuario}')
                return cursor.rowcount

if __name__ == '__main__':
    #insertar objeto
    usuario1 = Usuario(placa="JJJ-123",marca="Hino",color="verde",fecha="02/03/2022")
    usuarios_insertados = UsuarioDAO.insertar(usuario1)
    log.debug(f'Usuarios insertadas: {usuarios_insertados}')

    #Seleccionar objetos
    usuarios = UsuarioDAO.seleccionar()
    for usuario in usuarios:
        log.debug(usuario)