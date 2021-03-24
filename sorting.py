#pangram = "The quick brown fox jumps over the lazy dog"
panagramspasnish = "Benjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú"

orderspanish = sorted(panagramspasnish)
print(orderspanish)

missingletter = sorted("enjamín pidió una bebida de kiwi y fresa. Noé, sin vergüenza, la más exquisita champaña del menú",
                       key=str.casefold)
print(missingletter)

names = ["Jose",
         "Pepe",
         "pepe",
         "eric",
         "Terry",
         "joselito",
        ]
names.sort(key=str.casefold)
print(names)