lugares = {}
pesquisa = True

while pesquisa:
    nome = input("\nPor favor, informe o seu nome: ")
    lugar = input("\nSe pudesse visitar qualquer lugar do mundo, para onde você iria? ")
    
    lugares[nome] = lugar
    
    repete = input("\nDeseja repetir a pergunta para mais alguém? (sim/nao) ")
    
    if repete == 'nao':
        pesquisa = False
        
print("\nRespostas da pesquisa:")

for nome, lugar in lugares.items():
    print(f"{nome} gostaria de visitar {lugar}")
        
    