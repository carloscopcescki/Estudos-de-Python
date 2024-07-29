def city_country(cidade, pais):
    cidade_completa = cidade + ', ' + pais
    return cidade_completa

mensagem = city_country('São Paulo', 'Brasil')
print(mensagem) 