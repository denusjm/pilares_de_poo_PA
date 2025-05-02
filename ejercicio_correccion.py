class Dog:
    def __init__(self, name):
        self.name = name  #se corrige self.name para guardar el nombre como atributo del objeto. 
    def speak(self):
        return "woof"

dog = Dog("Bobby")
print(dog.name)
