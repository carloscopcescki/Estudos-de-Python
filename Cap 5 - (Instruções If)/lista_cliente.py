ingredientes_pizza = ['champignon', 'mussarela', 'calabresa', 'catupiry', 'bacon']

ingredientes_solicitados = ['azeitona', 'palmito', 'bacon']

for ingrediente_solicitado in ingredientes_solicitados:
    if ingrediente_solicitado in ingredientes_pizza:
        print(f"Adicionando {ingrediente_solicitado} na pizza.")
    else:
        print(f"Desculpe, não temos {ingrediente_solicitado}")

print("\nA sua pizza está pronta!")