class Car:
    """Simples tentativa de representar um carro"""
    def __init__(self, make, model, year) -> None:
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        pass
    
    def get_descriptive_name(self):
        '''Nome completo do modelo do carro'''
        long_name = f'{self.year} {self.make} {self.model}'
        return long_name.title()
    
    def read_odometer(self):
        '''Exibir uma frase indicando kilometragem do carro'''
        print(f"Esse carro está rodando a {self.odometer_reading}Km/h.")
        
    def update_odometer(self, mileage):
        '''Define a leitura do hodômetro para o valor fornecido'''
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print('Não é possível reverter o hodômetro.')
            
    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers
        
my_car = Car('GM', 'Onix', 2013)
print(my_car.get_descriptive_name())

my_car.update_odometer(23)
my_car.read_odometer()

my_car.increment_odometer(20)
my_car.read_odometer()