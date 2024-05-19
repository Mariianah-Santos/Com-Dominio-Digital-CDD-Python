class Animal():
    def __init__(self, nome, especie, idade):
        self.nome = nome
        self.especie = especie
        self.idade = idade
    def peso_animal(self, peso):
        self.peso = peso
        if (self.peso >= 5):
            print("Esta acima do peso")
        else:
            print("Esta abaixo do peso")

nome_animal = input("NOME: ")
animal1 = Animal(nome_animal, "Cachorro", 5)
pesoAnimal = float(input("PESO: "))
animal1.peso_animal(pesoAnimal)
print(animal1.especie, animal1.idade)