from queue import Queue

class Pila:

    def __init__(self):
        self._cola = Queue()

    def apilar(self, valor):
        self._cola.put(valor)

    def desapilar(self):
        return self._cola.get()

    def esta_vacia(self):
        return self._cola.empty()
