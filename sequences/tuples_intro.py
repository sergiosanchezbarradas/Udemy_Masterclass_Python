metallica = "Ride", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])

title, artista, year = metallica
print(title)
print(artista)
print(year)

table = ("Coffee table", 200, 100, 75, 32.56)
# print(table[1] * table[2])

# Make code mode readable by unpacking the tuple
name, length, width, height, price = table
print(length * width)
print(price + price)
