from nested_data import albums

while True:
    print("choose album (invalid exits):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}, {}, {}, {}"
              .format(index + 1, title, artist, year, songs))

    for index, value in enumerate(albums):
        title, artist, year, songs = value
        print(index + 1, title, artist, year, songs)

    break