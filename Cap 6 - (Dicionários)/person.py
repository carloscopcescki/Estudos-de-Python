pessoa = {
    'first name': 'carlos',
    'last name': 'alcarria',
    'age': '22',
    'city': 'são paulo',
}

primeiro_nome = pessoa['first name'].title()
sobrenome = pessoa['last name'].title()
cidade = pessoa['city'].title()

print(f"A pessoa se chama {primeiro_nome} {sobrenome}, possui {pessoa['age']} anos e mora em {cidade}")