class Car:
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

class Battery:
    '''Modelando uma bateria para o carro elétrico'''
    def __init__(self, battery_size):
        self.battery_size = battery_size
        
    def describe_battery(self):
        '''Descreve a capacidade da bateria'''
        print(f"Este carro possui uma carga atual de {self.battery_size}kWh")

class ElectricCar(Car):
    def __init__(self, make, model, year, battery=40):
        super().__init__(make, model, year)
        self.battery = Battery(battery)
        
    def fill_gas_tank(self):
        '''Carros elétricos não têm tanques de gasolina'''
        print("Esse carro não precisa de tanque de gasolina.")        

my_tesla = ElectricCar('tesla', 'model s', 2016, 89)
my_tesla.get_descritive_name()
my_tesla.fill_gas_tank()
my_tesla.battery.describe_battery()