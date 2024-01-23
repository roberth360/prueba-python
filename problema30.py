class Pila:

    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        return self.elementos.pop()

    def es_vacia(self):
        return len(self.elementos) == 0


class PilaLimitada(Pila):

    def __init__(self, limite):
        super().__init__()
        self.limite = limite

    def push(self, elemento):
        if len(self.elementos) >= self.limite:
            raise ValueError("La pila está llena")
        super().push(elemento)

    def esta_llena(self):
        return len(self.elementos) == self.limite
        
        
pila_limitada = PilaLimitada(5)

pila_limitada.push(1)
pila_limitada.push(2)
pila_limitada.push(3)
pila_limitada.push(4)

try:
    pila_limitada.push(5)
except ValueError:
    print("La pila está llena")

print(pila_limitada.esta_llena())
