def usuarios(nomes):
    for nome in nomes:
        msg = (f"Olá, {nome.title()}")
        print(msg)

lista_alunos = ['carlos', 'anderson', 'gabriel', 'mayra', 'ludmilla', 'kaique']

usuarios(lista_alunos)