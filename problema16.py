class Persona:
 

  def __init__(self, nombre, edad):
    
    self.nombre = nombre
    self.edad = edad

  def imp_detal(self):
   
    print(f"Nombre: {self.nombre}")
    print(f"Edad: {self.edad}")


persona = Persona("Roberth", 44)

persona.imp_detal()
