from empleado import Empleado


class Administrativo(Empleado):
    def calcular_bonificacion(self):
        return self.salario * 0.10