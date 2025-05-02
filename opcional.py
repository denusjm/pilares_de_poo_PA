#Desafío opcional
#Agregá encapsulamiento con atributos privados y métodos get y set.
class Vehiculo: 
  def __init__(self,marca): 
      self._marca = marca

  def get_marca(self): 
      return self._marca

  def set_marca(self, nueva_marca):
      self._marca = nueva_marca 

  def descripcion(self): 
      return f"vehiculo de marca {self._marca}"

class Auto(Vehiculo):
  def descripcion(self): 
     return f"Auto es de la marca {self.get_marca} y tiene 4 ruedas"

class Bicicleta(Vehiculo):
  def descripcion(self):
     return f"Bicicleta es de la marca {self.get_marca} y tiene 2 ruedas" 

def mostrar_descripcion(Vehiculo):
  print(vehiculo.descripcion)

v1 = Auto("Toyota") 
v2 = Bicicleta("Biker") 

mostrar_descripcion(v1)
mostrar_descripcion(v2)
