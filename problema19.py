class Persona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def imprimir_detalles(self):
        print("Nombre:", self.nombre)
        print("Apellido:", self.apellido)
        print("Edad:", self.edad)


class Estudiante(Persona):

    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido, edad)
        self.carrera = carrera

    def imprimir_detalles(self):
        super().imprimir_detalles()
        print("Carrera:", self.carrera)

estudiante = Estudiante("Roberth", "Aragón", 30, "Ingeniería Informatica")

estudiante.imprimir_detalles()
