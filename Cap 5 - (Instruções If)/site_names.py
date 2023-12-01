current_users = ['carlos', 'mayra', 'carol', 'kaique', 'luiza']
new_users = ['zonta', 'ludmilla', 'carol', 'luiza', 'nicolas']

for new_user in new_users:
    if new_user in current_users:
        print(f"Olá {new_user.title()}, favor inserir um nome novo de usuário.")
    else:
        print(f"Olá {new_user.title()}, o seu nome está disponível para cadastro.")
    