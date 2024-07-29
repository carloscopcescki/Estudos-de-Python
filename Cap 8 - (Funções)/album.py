def make_album(name, title):
    album = {'nome': name, 'album': title}
    return album

pink_floyd = make_album('Pink Floyd', 'The Wall')
beatles = make_album('The Beatles', 'Revolver')
beach_boys = make_album('The Beach Boys', 'Pet Sounds')

print(pink_floyd)
print(beatles)
print(beach_boys)