#Ejercicio:
#Define una jerarquía simple para vehículos con al menos una clase base y dos clases hijas.
#Cada clase hija debe tener un método propio sobrescrito que imprima información
#diferente. Crea una función que reciba un vehículo y llame a ese método.






class vehiculo:
    def descripcion(self): 
        return "Soy un vehiculo" 
        
class Auto(vehiculo): 
    def descripcion(self): 
        return "Soy un auto de 4 ruedas"
        
class Bicicleta(vehiculo):
    def descripcion(self): 
        return "Soy una bicicleta de 2 ruedas"
        
def mostrar_descripcion(vehiculo): 
    print(vehiculo.descripcion())
    
v1 = Auto()
v2 = Bicicleta()

mostrar_descripcion(v1)
mostrar_descripcion(v2)
