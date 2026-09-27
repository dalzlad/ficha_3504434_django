from producto import Producto

class Producto_Perecedero(Producto):

    def __init__(self,id,nombre,precio,stock,fecha_vencimiento):
        super().__init__(id,nombre,precio,stock)
        self.fecha_vencimiento = fecha_vencimiento