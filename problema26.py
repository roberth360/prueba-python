class Circulo:

    def __init__(self, radio, color):
        self.radio = radio
        self.color = color

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def __str__(self):
        return f"Circulo de radio {self.radio} y color {self.color}"
circulo = Circulo(5, "rojo")

print(circulo)
