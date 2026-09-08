from abc import ABC, abstractmethod

class Empleado(ABC):
    def __init__(self, nombre, documento, salario): #constructor de la clase
        self.nombre = nombre #Atributo
        self.documento = documento #Atributo
        self.__salario = salario #Atributo

    @abstractmethod #Método abstracto
    def calcular_bonificacion(self):
        pass

    @property #Accediendo a un atributo privado
    def salario(self):
        return self.__salario

    def mostrar_informacion(self): #Método
        print(f"Nombre: {self.nombre}")
        print(f"Documento: {self.documento}")
        print(f"Salario: {self.salario:,0.f}")

    
    def __str__(self): #Método
        return f"Nombre: {self.nombre} - Documento: {self.documento}"