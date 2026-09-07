from empresa.empleado import Empleado


class Desarrollador(Empleado):
    def calcular_bonificacion(self):
        return self.salario*0.15