class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descritive_name(self):
        long_name = print(f"{self.model} {self.make} {self.year}")
        return long_name
    
    def read_odometer(self):
        print(f"Este carro está rodando a {self.odometer_reading}Km/h.")
    
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("Não é possível alterar")
        
    def increment_odometer(self, kilometers):
        self.odometer_reading += kilometers

class ElectricCar(Car):
    '''Representa aspectos específicos de carros elétricos'''
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery_size = 70
    
    def describe_battery(self):
        '''Descreve a capacidade da bateria'''
        print(f"Esse carro possui {self.battery_size}kWh bateria")
        
    def fill_gas_tank(self):
        '''Carros elétricos não têm tanques de gasolina'''
        print("Esse carro não precisa de tanque de gasolina.")

my_tesla = ElectricCar('tesla', 'model s', 2016)
my_tesla.get_descritive_name()
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
