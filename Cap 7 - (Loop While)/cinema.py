print("Ingressos Cinema")

active = True

while active:
    try:
        idade = int(input("\nInforme a sua idade: "))
        
        if idade < 3:
            print("\nIngresso gratuito.")
        elif idade >= 3 and idade <= 12:
            print("\nO ingresso custa US$10")
        elif idade > 12:
            print("\nO ingresso custa US$15")
        else:
            print("\nDigite um valor válido.")
            break
    except:
        print("\nValor inválido.")
        break
