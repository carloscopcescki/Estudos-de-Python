pizzas = ['mussalera', 'calabresa', 'catupiry']

friend_pizzas = pizzas[:]

pizzas.append('mista')
friend_pizzas.append('marguerita')

print("Minhas pizzas favoritas são:")

for pizza in pizzas:
    print(pizza)

print("\nAs pizzas favoritas do meu amigo são estas:")

for pizza_amigo in friend_pizzas:
    print(pizza_amigo)
