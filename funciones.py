from auto_DAO import UsuarioDAO
import datetime
from logger import log


def Registrar(usuario):
    Usuarios = UsuarioDAO().seleccionar()
    if (not Usuarios is None):
        for i in range(len(Usuarios)):
            if usuario.placa == Usuarios[i].placa:
                usuario.fecha == datetime.datetime.now()
        UsuarioDAO().insertar(usuario)
        return print("Registro satisfactorio")
    else:    
        UsuarioDAO().insertar(usuario)
        return print("Registro satisfactorio")

def Ver_registro():
    usuarios = UsuarioDAO().seleccionar()
    for usuario in usuarios:
        log.debug(usuario)
