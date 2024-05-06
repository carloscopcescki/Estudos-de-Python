alien = {'cor':'azul', 'pontos':'5'}

pontos = alien['pontos']

print(f"Você obteve {pontos} pontos por abater a nave!")

del alien['pontos']
print(alien)

valor_ponto = alien.get('pontos', 'Não possui ponto')
print(valor_ponto)