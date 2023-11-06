jantar = ['mudo', 'almir', 'josé']

nao_vai = jantar.pop(0)
jantar.insert(0,'leonardo')

print(f"O {nao_vai.title()} não poderá ir ao jantar")
print(f"O {jantar[0].title()}, irá no lugar do {nao_vai.title()}")