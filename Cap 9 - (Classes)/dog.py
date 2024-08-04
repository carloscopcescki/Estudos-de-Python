class Dog:
    """Modelar um cachorro"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"{self.name} está sentando.")
    
    def roll_over(self):
        print(f"{self.name} está rolando")
        
cachorro = Dog('Mel', 12)

print(f"O meu cachorro se chama {cachorro.name}.")
print(f"E possui {cachorro.age} anos.")

cachorro.sit()
cachorro.roll_over()