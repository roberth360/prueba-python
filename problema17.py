class Rectangulo:

  def __init__(self, ancho, altura):
    
    self.ancho = ancho
    self.altura = altura

  def calcular_area(self):
    
    return self.ancho * self.altura

  def calcular_perimetro(self):
    
    return 2 * (self.ancho + self.altura)



rectangulo = Rectangulo(13, 250)

print(rectangulo.calcular_area())  
print(rectangulo.calcular_perimetro()) 
