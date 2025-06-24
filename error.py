class DimensionError(Exception):
    def __init__(self,mensaje,dimension, maximo):
        self.mensaje=mensaje
        self.dimension=dimension
        self.maximo=maximo
    
    def __str__(self):
        if self.dimension is None and self.dimension is None:
            return super().__str__() ## el super me permite traer la clase padre
        else:
            return f"{self.mensaje} {self.dimension} {self.maximo}"
    
    
    pass