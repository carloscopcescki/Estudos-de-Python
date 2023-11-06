print("Digite a sua idade:")

idade = int(input())

if idade < 16:
    print("Você não poderá assistir ao filme")
elif idade >= 16 and idade < 18:
    print("Você só pode ver o filme acompanhado dos pais!")
else:
    print("Você poderá assistir o filme!")