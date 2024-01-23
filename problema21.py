class Cola:

    def __init__(self):
        self._cola = []

    def encolar(self, valor):
        self._cola.append(valor)

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError("La cola está vacía")
        return self._cola.pop(0)

    def esta_vacia(self):
        return len(self._cola) == 0
