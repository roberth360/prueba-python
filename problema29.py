class Matriz:

    def __init__(self, filas, columnas, valores):
        self.filas = filas
        self.columnas = columnas
        self.valores = valores

    def __repr__(self):
        return "Matriz({}, {}): {}".format(self.filas, self.columnas, self.valores)

    def sumar(self, otra_matriz):
        if self.filas != otra_matriz.filas or self.columnas != otra_matriz.columnas:
            raise ValueError("Las matrices deben tener el mismo número de filas y columnas")

        nueva_matriz = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                nueva_matriz.valores[i][j] = self.valores[i][j] + otra_matriz.valores[i][j]
        return nueva_matriz

    def multiplicar_por_escalar(self, escalar):
        nueva_matriz = Matriz(self.filas, self.columnas)
        for i in range(self.filas):
            for j in range(self.columnas):
                nueva_matriz.valores[i][j] = self.valores[i][j] * escalar
        return nueva_matriz

matriz_1 = Matriz(2, 3, [[1, 2, 3], [4, 5, 6]])
matriz_2 = Matriz(2, 3, [[7, 8, 9], [10, 11, 12]])

matriz_suma = matriz_1.sumar(matriz_2)
print(matriz_suma)

matriz_multiplicacion = matriz_1.multiplicar_por_escalar(2)
print(matriz_multiplicacion)
