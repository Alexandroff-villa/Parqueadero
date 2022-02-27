print("-------BIENVENIDO AL PARQUEDERO-------")

import datetime
ddatos = {}
num_carro = 0
opc = ""

while opc != "s":
    print("a. Registrar servicio")
    print("b. Ver servicio")
    print("d. Finalizar servicio")
    print("s. Salir")

    opc = input("ingrese la opción deseada: ")

    if (opc == 'a'):
        print("-------ESCOGISTE INICIAR SERVICIO------")
        mat=input("Ingrese el numero de su matricula: ")
        if num_carro != 0:
            for i in range(num_carro):
                if mat == ddatos[i]["matricula"]:
                    print("su auto es recurrente")
                    fecha = datetime.datetime.now()
                    ddatos[num_carro]={"matricula":mat,"placa":pl,"marca":marca,"color":color,"fecha":fecha}
                    num_carro +=1
        else:            
            pl = input("Ingrese el numero de su placa: ")
            marca = input("Ingrese la marca de su vehiculo: ")
            color = input("Ingrese el color de su vehiculo: ")
            fecha = datetime.datetime.now()
            ddatos[num_carro]={"matricula":mat,"placa":pl,"marca":marca,"color":color,"fecha":fecha}
            num_carro +=1

    elif (opc == 'b'):
        print("-------VER REGISTROS------")
        for k in ddatos.keys():
            print("mat:",ddatos[k]["matricula"])
            print("marca:",ddatos[k]["marca"])
            print("pl:",ddatos[k]["placa"])
            print("color:",ddatos[k]["color"])
            print(str(fecha))

    elif (opc == "d"):
        print("------ESCOGISTE FINALIZAR EL SERVICIO------")

    else:
        break