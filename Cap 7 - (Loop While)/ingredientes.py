print("Ingredientes para pizza")

active = True
mensagem = ""
ingredientes = []

while active:
    mensagem = input("\nInforme um ingrediente da pizza: ")
    ingredientes.append(mensagem)
    if mensagem != 'quit':
        continue
    else:  
        active = False
        print(f"\nTodos os ingredientes da pizza: {ingredientes[:-1]}")