import math

# Programa para calcular a equação de 2° grau utlizando a fórmula de Bhaskara
print("Programa Equação 2° Grau")

# Exemplo de equação de 2° grau
# X² - 5x + 6 = 0
a = float(input("\nDigite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

# Valor de delta (Δ)
# Δ = b² - 4 * A * C
def calculo_delta(a,b,c):
    b = b**2
    delta = b - 4 * (a) * (c)
    return delta

delta = calculo_delta(a,b,c)
raiz_delta = math.sqrt(delta)

print(f"\nO valor de Δ é: {delta}")


# Fórmula de Bhaskara
# X = −b ± √​​Δ / 2a
def formula_bhaskara_x1(b,a,raiz_delta):
    x1 = (-(b) + raiz_delta) / (2 * a)
    return x1

def formula_bhaskara_x2(b,a,raiz_delta):
    x2 = (-(b) - raiz_delta) / (2 * a)
    return x2

x1 = formula_bhaskara_x1(b,a,raiz_delta)
x2 = formula_bhaskara_x2(b,a,raiz_delta)

print(f"\nO valor de X1 é: ", x1)
print(f"\nO valor de X2 é: ", x2)
   
    