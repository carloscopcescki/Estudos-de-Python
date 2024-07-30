def sanduiches(*lanches):
    for lanche in lanches:
        print(f"- {lanche.title()}")

print("\nLista de lanches do Carlos:")
sanduiches('pão com mortadela')
sanduiches('hamburguer', 'x-bacon')