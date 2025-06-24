from error import DimensionError

class Foto():

    max =2500

    def __init__ (self, ancho:int, alto:int, ruta:str) -> None:
        self.__ancho = ancho
        self.__alto = alto
        self.__ruta = ruta

    @property
    def ancho(self) -> int:
        return self.__ancho
    
    @ancho.setter
    def ancho(self, ancho) -> None:
        self.__ancho = ancho


    @property
    def alto(self) -> int:
        return self.__alto
    
    
    @alto.setter
    def alto(self, alto) -> None:
        self.__alto = alto