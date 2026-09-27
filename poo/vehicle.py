class Vehicle:
    """plate
    color
    brand"""
    def __init__(self, plate, color, brand): #Constructor
        self.plate = plate
        self.color = color
        self.brand = brand

    def mover(self):
        print("El vehículo se mueve")

class Car(Vehicle):#Herencia
    pass

class Motorbike(Vehicle):#Herencia
    def desplegar_gato(self):
        print("Gato desplegado")

class truck(Vehicle):
    def cargar(self):
        print("Cargar Coca_Cola")


car1 = Car('666AAA','black','MAZDA')
print(car1.plate)
car1.mover()

motorbike1 = Motorbike('HK77','yellow','YAMAHA')
motorbike1.mover()
motorbike1.desplegar_gato()

#Por equipos de 2
1.Diagrama de clases
# Crear un gráfico con la clase Figura y el atributo largo.
# Crear la clase Círculo y Cuadrado con los métodos calcular área y calcular perímetro.

2.Programar en python la clases del gráfico anterior con sus respectivos atributos y métodos





#Realizar un POO que permita calcular a través de un método:
# el valor del descuento de un producto.

#Si la cantidad de productos es inferior a 10 el descuento es del 5%.
#Si la cantidad de productos es mayor a 10 e inferior a 50 el descuento es del 10%
#Si es >= 49 el descuento es del 12.5 
#No se pueden realizar cálculos con cantidades negativas o iguales a cero.
#Los atributos de la clase son:
#son id, nombre, cantidad, y precio.
#Crear 2 objetos para verificar el funcionamiento de los descuentos.

