mystring = 'Heya'

# mylist = []

# for letter in mystring:
#     mylist.append(letter)
# print(mylist)

#better way
mylist = [letter for letter in mystring]
print(mylist)

milista = [x for x in 'perrote']
print(milista)

numeros = [num for num in range(0,11)]
print(numeros)

#print only evens
pares = [x for x in range(0,51) if x%2==0]
print(pares)