users = ['carlos', 'mayra', 'zonta', 'di levs', 'ludmillo', 'admin']

for user in users:
    if user == 'admin':
        print(f"Olá {user.title()}, gostaria de ver um relatório de status?")
    else:    
        print(f"Olá {user.title()}, seja bem vindo!")