from logger import log
import pymysql.cursors
import sys

class Conexion:
    _DATABASE = 'tienda'
    _USERNAME = 'root'
    _PASSWORD = '23deAbril'
    _HOST = '127.0.0.1'
    _conexion = None
    _cursor = None

    @classmethod
    def obtenerConexion(cls):
        if cls._conexion is None:
            try:
                cls._conexion = pymysql.connect(host=cls._HOST,
                                          user = cls._USERNAME,
                                          database = cls._DATABASE,
                                          password = cls._PASSWORD)
                log.debug(f'conexion existosa: {cls._conexion}')
                return cls._conexion
            except Exception as e:
                log.debug(f'Ocurrio una excepcion al obtener la conexion {e}')
                sys.exit()
        else:
            return cls._conexion

    @classmethod
    def obtenerCursor(cls):
        if cls._cursor is None:
            try:
                cls._cursor = cls.obtenerConexion().cursor()
                log.debug(f'se abrio correctamente el cursor: {cls._cursor}')
                return cls._cursor
            except Exception as e:
                log.error(f'Ocurrio una excepcion al obtener el cursor: {e}')
                sys.exit()
        else:
            return cls._cursor

if __name__=='__main__':
    Conexion.obtenerConexion()
    Conexion.obtenerCursor()