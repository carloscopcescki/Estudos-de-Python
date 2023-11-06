jantar = ['mudo', 'almir', 'josé', 'leonardo']

print("\tInfelizmente a mesa é pequena, terei que reduzir os convidados!")

convidado_1 = jantar.pop(0)

print(f"{convidado_1.title()}, infelizmente você foi removido da lista!")

convidado_2 = jantar.pop(0)

print(f"{convidado_2.title()}, infelizmente você foi removido da lista!")

print(f"A lista agora contém apenas o {jantar[0].title()} e o {jantar[1].title()}")

del jantar[0]
del jantar[0]

print("A lista agora está vazia:", jantar)