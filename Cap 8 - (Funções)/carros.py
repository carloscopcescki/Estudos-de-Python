def make_car(marca, modelo, **info):
    info['marca_carro'] = marca
    info['modelo_carro'] = modelo
    return info

car = make_car('gm', 'celta', cor='preto', motor='1.0')
car_two = make_car('ford', 'ka', cor='prata', motor='1.5')

print(car)
print(car_two)