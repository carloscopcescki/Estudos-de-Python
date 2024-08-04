class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.name = restaurant_name
        self.type = cuisine_type
    
    def describe_restaurant(self):
        print(f"O restaurante se chama {self.name} e possui o tipo {self.type} de culinária")
    
    def open_restaurant(self):
        print(f"{self.name} está aberto no momento.")
        
estrela = Restaurant('Estrela', 'churrasco')
fogo_chao = Restaurant('Fogo de Chão', 'carnes')
pizzaria = Restaurant('Pizzaria Itália', 'pizzas')

estrela.describe_restaurant()
fogo_chao.describe_restaurant()
pizzaria.describe_restaurant()