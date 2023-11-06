carros_gm = ['celta', 'corsa', 'onix', 'montana', 's10', 'tracker', 'cobalt']

#Para remover itens de uma lista, podemos utilizar pop ou del. Com pop podemos utilizar o dado removido para outras funcionalidades.

print(carros_gm)
ultimo = carros_gm.pop(2)
print(f"O último carro adquirido foi: {ultimo.title()}")

carros_gm.append('carroça')
print(carros_gm) 