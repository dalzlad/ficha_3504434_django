
class Producto:
    def __init__(self,id,nombre, precio, stock):
        self.id = id
        self.nombre= nombre
        self.precio = precio
        self.stock = stock

    def Aumentar_Stock(self):
        self.stock+=1
        return self.stock

    def Disminuir_Stock(self):
        self.stock-=1
        return self.stock