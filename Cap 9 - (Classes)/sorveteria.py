class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"O restaurante se chama {self.name} e possui o tipo {self.type} de culinária")
    
    def open_restaurant(self):
        print(f"{self.name} está aberto no momento.")
        
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type) -> None:
        super().__init__(restaurant_name, cuisine_type)
    
    def flavor_list(self):
        sorvetes = ['Chocolate', 'Flocos', 'Napolitano', 'Creme', 'Romeu e Julieta']
        self.flavors = []
        print("Lista de sorvetes: \n")
        while sorvetes:
            sorvete = sorvetes.pop()
            self.flavors.append(sorvete)
        
        for flavor in self.flavors:
            print(flavor)

restaurante = IceCreamStand('Sorveteria do Carlos', 'Sorveteria')
restaurante.flavor_list()

            