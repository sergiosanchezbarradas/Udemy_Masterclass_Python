# for index, character in enumerate("abcdefghijklmnopqrstuvwxyz"):
#     print(index + 1, character)

# for i in enumerate("abcdefghijklmnopqrstuvwxyz"):
#     print(i)

# we are unpacking the tuple as we are iterating
for t in enumerate("abcdefghij"):
    index, character = t
    print(index, character)