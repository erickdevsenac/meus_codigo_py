class Animal:
    def emite_som(self):
        print('O animal faz um som')
        
class Cachorro(Animal):
    def emite_som(self):
        print("O chachorro late")

class Gato(Animal):
    def emite_som(self):
        print("O gato mia")
    
def emitir_som(animal):
    animal.emite_som()

bichos = [Cachorro(), Gato(), Animal()]

for bicho in bichos:
    emitir_som(bicho)