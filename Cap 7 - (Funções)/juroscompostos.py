# Programa desenvolvido para calcular juros compostos
# Fórmula de juros compostos || M = C * (1 + t)^i 
# M = Montante total
# C = Valor inicial)
# t = Taxa de juros
# i = Tempo

print("Programa Juros Compostos")

# Insira os valores para calcular os juros compostos
capital = float(input("\nInforme o valor inicial: "))
aporte_mensal = float(input("Informe o valor a ser depositado mensalmente: "))
taxa_juros = float(input("Informe a taxa de juros anual: "))
tempo_anos = float(input("Tempo (anos): "))

meses = int(tempo_anos * 12)
deposito = 0
total = capital
taxa_juros_ano = (taxa_juros / 100)
taxa_juros_mes = ((1 + taxa_juros_ano)**(1/12) - 1) * 100

# Laço de repetição para calcular o montante de juros por mês (de acordo com o total de anos e o valor mensal a ser aportado)
for vezes in range(1, (meses + 1)):
    deposito += aporte_mensal
    total += (total * (taxa_juros_mes / 100))
    total += aporte_mensal

# Função para calcular os juros compostos com aporte mensal
def juros_compostos(capital,taxa_juros_ano,tempo_anos):
    montante = capital * ((1 + taxa_juros_ano)** tempo_anos)
    juros = (montante - capital)
    return juros

# Função para calcular juros compostos simples (sem aporte mensal)
def juros_compostos_mensal(total,capital, deposito):
    deposito = deposito + capital
    juros = total - deposito
    return juros
    
if aporte_mensal > 0:
    jc = juros_compostos_mensal(total,capital, deposito)
    valor_investido = (capital + (aporte_mensal * meses))
    montante = (valor_investido + jc)
    jc = montante - valor_investido
    print(f"\nO montante total é: R$ {montante:.2f}")
    print(f"O valor investido foi: R$ {valor_investido}")
    print(f"O total em juros é: R$ {jc:.2f}")  
elif aporte_mensal <= 0:
    jc = juros_compostos(capital,taxa_juros_ano,tempo_anos)
    montante = (capital + jc)
    jc = montante - capital
    print(f"\nO montante total é: R$ {montante:.2f}")
    print(f"O valor investido foi: R$ {capital}")
    print(f"O total em juros é: R$ {jc:.2f}")
else:
    print("\nValor invalido!")

    

    
        
