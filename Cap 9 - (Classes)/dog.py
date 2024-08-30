class Dog:
    """Modelar um cachorro"""
    
    def __init__(self, name, age, race):
        self.name = name
        self.age = age
        self.race = race
        
    def sit(self):
        print(f"{self.name} está sentando.")
    
    def roll_over(self):
        print(f"{self.name} está rolando")

name = input("Qual o nome do seu dog: ")
age = int(input("\nQual a idade do seu dog: "))
race = input("\nQual a raça do seu dog: ")

cachorro = Dog(name, age, race)

print(f"O nome do meu dog é {cachorro.name}, ele tem {cachorro.age} anos e é da raça {cachorro.race}")