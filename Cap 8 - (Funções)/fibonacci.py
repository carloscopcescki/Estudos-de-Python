print("Programa Série Fibonacci")

num1 = 0
num2 = 1
num3 = 0

total_num = []
serie = int(input("\nInforme a quantidade de termos para a série Fibonacci: "))

contador = 1

while (contador <= serie):
    total_num.append(num1)
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    contador += 1
    
print("\nSérie de Fibonacci: ",total_num)