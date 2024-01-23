class ÁrbolBinario:

    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

    def insertar(self, valor):
        if valor < self.valor:
            if self.izquierdo is None:
                self.izquierdo = ÁrbolBinario(valor)
            else:
                self.izquierdo.insertar(valor)
        else:
            if self.derecho is None:
                self.derecho = ÁrbolBinario(valor)
            else:
                self.derecho.insertar(valor)

    def recorrer_en_orden(self):
        if self.izquierdo is not None:
            self.izquierdo.recorrer_en_orden()
        print(self.valor)
        if self.derecho is not None:
            self.derecho.recorrer_en_orden()

    def buscar(self, valor):
        if self.valor == valor:
            return True
        elif valor < self.valor and self.izquierdo is not None:
            return self.izquierdo.buscar(valor)
        elif valor > self.valor and self.derecho is not None:
            return self.derecho.buscar(valor)
        else:
            return Falsearbol.recorrer_en_orden()


arbol = ÁrbolBinario(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)
arbol.insertar(12)
arbol.insertar(17)

arbol.recorrer_en_orden()

print(arbol.buscar(5))
