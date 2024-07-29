def make_album(name, title):
    album = {'nome': name, 'album': title}
    return album

while True:
    print("\nInforme o seu artista e o seu album favorito!")
    print("\nDigite 'q' para sair.")
    artista = input("\nNome do artista: ")
    album_artista = input("Album: ")
    if artista == 'q':
        break
    if album_artista == 'q':
        break
    print("\nArtistas favoritos:")
    fav_artista = make_album(artista, album_artista)
    print(f"\n{fav_artista}")
