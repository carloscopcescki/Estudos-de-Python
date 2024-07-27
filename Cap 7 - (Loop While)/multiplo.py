# Informe se o número é múltiplo de 10

número = int(input("Digite um número: "))

multiplo = número % 10

if multiplo == 0:
    print(f"\nO número digitado é múltiplo de 10.")
else:
    print(f"\nO número digitado não é múltiplo de 10.")