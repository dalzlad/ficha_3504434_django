from administrativo import Administrativo
from desarrollador import Desarrollador
from gerente import Gerente


def main():
    administrativo = Administrativo('Ximena','8989',1000)

    print(administrativo)

    print(administrativo.salario)

    desarrollador = Desarrollador('Ana',6400,1100,'Chatear')
    print(desarrollador)
    print(desarrollador.calcular_bonificacion())

    gerente = Gerente('Lyne',2323, 8000)
    print(gerente.calcular_bonificacion())

if __name__ == "__main__":
    main()



###Realizar un programa orientado a objetos en python que permita
##Calcular el volumen de un cilindro, esfera y cubo
##Aplicar herencia, polimorfismo, abstracción
##Crear objetos. Crear una clase para cilindro otra para esfera y otra para
#cubo

##Cargar el proyecto a git.
#1. Crear la carpeta geometria
#2. Crear el archivo figura.py
#3. Crear el archivo esfera.py V= 4/3 * pi * radio*radio*radio
#4. Crear el archivo cilindro.py V= pi * radio*radio*altura
#5. Crear el archivo cubo.py V= largo*largo*largo
#6  Crear el archivo main.py
#https://github.com/dalzlad/ficha_3504434_django