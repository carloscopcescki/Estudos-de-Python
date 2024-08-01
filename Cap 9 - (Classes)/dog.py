class Dog:
    """Modelar um cachorro"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def sit(self):
        print(f"O {self.name} está sentando.")
    
    def roll_over(self):
        print(f"O {self.name} tem {self.age} anos.")
        
