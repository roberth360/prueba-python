class Empleado:

    def __init__(self, nombre, salario, aumento):
        self.nombre = nombre
        self.salario = salario
        self.aumento = aumento

    def calcular_salario_actualizado(self):
        return self.salario * (1 + self.aumento)


empleado = Empleado("Roberto Aragón", 1000, 0.10)

salario_actualizado = empleado.calcular_salario_actualizado()

print (salario_actualizado)
