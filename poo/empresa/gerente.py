from empresa.empleado import Empleado


class Gerente(Empleado):
    def calcular_bonificacion(self):
        return self.salario*0.20