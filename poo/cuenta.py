class Cuenta:
    def __init__(self, numero,saldo):#Constructor
        self.numero = numero
        self.__saldo = saldo

    def Depositar(self, cantidad):#Métodos o comportamientos
        if cantidad > 0:
            self.__saldo += cantidad

    #Agregar el método retirar
    
    def ImprimirSaldo(self):
        print(f"El saldo de la cuenta {self.numero} es: {self.__saldo}")    

#Creación del objeto
cuenta1 = Cuenta(1111,1000)
cuenta1.Depositar(9999)
print(cuenta1.ImprimirSaldo())

#Crear un repositorio en git que contendrá todo lo que hará en django
#Subir este ejercicio a git.
#Enviarme el enlace a dilopezz@sena.edu.co antes de las 08:00 a.m
#Si no lo sube se le enviará un taller orientado a objetos
#para exponer mañana.
