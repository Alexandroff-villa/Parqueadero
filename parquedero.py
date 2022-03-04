print("-------BIENVENIDO AL PARQUEDERO-------")
from auto_DAO import UsuarioDAO
from funciones import Registrar, Ver_registro
import datetime

from usuario import Usuario
opc = ""

while opc != "s":
    print("a. Registrar servicio")
    print("b. Ver servicio")
    print("d. Finalizar servicio")
    print("s. Salir")

    opc = input("ingrese la opción deseada: ")

    if (opc == 'a'):
        print("-------ESCOGISTE INICIAR SERVICIO------")
        pl = input("Ingrese el numero de su placa: ")
        marca = input("Ingrese la marca de su vehiculo: ")
        color = input("Ingrese el color de su vehiculo: ")
        fecha = datetime.datetime.now()
        usuario = Usuario(placa=pl,marca=marca,color=color,fecha=fecha)
        Registrar(usuario)
        

    elif (opc == 'b'):
            Ver_registro()

    elif (opc == "d"):
            print("------ESCOGISTE FINALIZAR EL SERVICIO------")        


    elif (opc == "s"):
        break