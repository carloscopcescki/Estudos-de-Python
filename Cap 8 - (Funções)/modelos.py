# Percorre a lista dos modelos não impressos e adiciona na lista de modelos impressos.
def preparando_impressao(modelos_incompletos, modelos_completos):
    while modelos_incompletos:
        atual = modelos_incompletos.pop()
        print(f"Imprimindo modelo de: {atual.title()}")
        modelos_completos.append(atual)
    
# Exibir os modelos impressos
def impressao_completa(modelos_completos):
    print("\nOs modelos a seguir foram impressos na impressora 3D:")
    for modelo in modelos_completos:
        print(modelo.title())
    
modelos_incompletos = ['telefone', 'carro', 'espada']
modelos_completos = []

preparando_impressao(modelos_incompletos, modelos_completos)
impressao_completa(modelos_completos)