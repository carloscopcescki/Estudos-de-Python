users = ['admin']

for user in users:
    if users == []:
        print("É necessário encontrar alguns usuários")
    elif user == 'admin':
        print("Olá administrador, gostaria de ver um relatório de status?")
    else:
        print("Olá Jaden, obrigado por fazer login novamente.")
