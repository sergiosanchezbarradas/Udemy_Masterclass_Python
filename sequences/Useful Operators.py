# mylist = [1,2,3]
#
# for num in range(0,11,2):
#     print(num)
#
# abc_count = 1
# for letter in "abcdefghijklmnopqrstuvwxyz":
#     print("numero {} corresponde a la letra {}".format(abc_count,letter))
#     abc_count += 1

# or

word = 'abcdefghijklmnopqrstuvwxyz'

for index,letter in enumerate(word):
    print(index)
    print(letter)
    print('\n')

from random import shuffle
