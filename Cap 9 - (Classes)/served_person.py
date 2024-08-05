class Restaurant:
    def __init__(self, restaurant_name, cuisine_type) -> None:
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0
    
    def describe_restaurant(self):
        print(f"O restaurante se chama {self.name}, possui o tipo {self.type} de culinária e possui {self.number_served} pessoas hoje.")
    
    def open_restaurant(self):
        print(f"{self.name} está aberto no momento.")
        
    def servered_person(self, restaurant):
        self.number_served = restaurant
        
    def increment_person(self, person):
        self.number_served += person
            
    
estrela = Restaurant('Estrela', 'churrasco')

estrela.describe_restaurant()
estrela.servered_person(2)
estrela.increment_person(1)
estrela.describe_restaurant()

