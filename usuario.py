from logger import log


class Usuario:
    def __init__(self,id_carro=None,placa=None,marca=None,color=None,fecha=None):
        self._id_carro = id_carro
        self._placa = placa
        self._marca = marca
        self._color = color
        self._fecha = fecha

    def __str__(self):
        return f'''
                Id: {self._id_carro}, Placa: {self._placa}, Marca: {self._placa},
                Color: {self._color}, fecha: {self._fecha}
        '''
    
    @property
    def id_carro(self):
        return self._id_carro

    @id_carro.setter
    def id_carro(self,id_carro):
        self._id_carro = id_carro

    @property
    def placa(self):
        return self._placa

    @placa.setter
    def placa(self,placa):
        self._placa = placa

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self,marca):
        self._marca = marca

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self,color):
        self._color = color

    @property
    def fecha(self):
        return self._fecha

    @fecha.setter
    def fecha(self,fecha):
        self._fecha = fecha

if __name__=='__main__':
    vehiculo1 = Usuario(1,"III-123","Nissan","azul","02/03/2022")
    log.debug(vehiculo1)