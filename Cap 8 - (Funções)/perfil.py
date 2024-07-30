def profile(nome, sobrenome, **info):
    info['primeiro_nome'] = nome
    info['segundo_nome'] = sobrenome
    return info

informaçoes = profile('Carlos', 'Daniel', idade=22, profissão='Operador de Produção')

print(informaçoes)