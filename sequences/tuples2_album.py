albums =[("Album1", "Artista1", 1278),
          ("Album2", "Art2", 2001),
          ("Album3", "Art3", 1945),
          ("Album4", "Art4", 2076),
          ("Album5", "Art5", 1977),
          ]
print(len(albums))

for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {} "
          .format(name, artist, year))
