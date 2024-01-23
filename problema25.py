class Diccionario:

    def __init__(self):
        self._diccionario = {}

    def agregar(self, clave, valor):
        self._diccionario[clave] = valor

    def buscar(self, clave):
        if clave in self._diccionario:
            return self._diccionario[clave]
        else:
            return None

    def eliminar(self, clave):
        if clave in self._diccionario:
            del self._diccionario[clave]


diccionario = Diccionario()

diccionario.agregar("nombre", "Roberto Aragón")
diccionario.agregar("edad", 30)

valor_nombre = diccionario.buscar("nombre")
print(valor_nombre)
# Salida: Juan Pérez

diccionario.eliminar("edad")

print(diccionario.buscar("edad"))
