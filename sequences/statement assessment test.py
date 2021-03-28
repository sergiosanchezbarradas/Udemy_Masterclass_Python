# Use for, .split(), and if to create a
# Statement that will print out words
# that start with 's':

st1 = 'Print only the words that start with s in this sentence'
for s in st1.split():
    if s.startswith('s'):
        print(s)

#Use range() to print all the even numbers from 0 to 10.
pares = [par for par in range(0,11) if par%2==0]
print(pares)


#Use a List Comprehension to create a list
# of all numbers between 1 and 50 that are divisible by 3.
entre3 = [tres for tres in range(0,51) if tres%3==0]
print(entre3)

st2 = 'Print every word in this sentence that has an even number of letters'
for word in st2.split():
    if len(word)%2 == 0:
        print(word + " <-- has an even length!")

#Write a program that prints the integers from 1 to 100.
# But for multiples of three print "Fizz" instead of the number,
# and for the multiples of five print "Buzz".
# For numbers which are multiples of both three and five
# print "FizzBuzz".

for num in range(1,101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)

st100 = 'Create a list of the first letters of every' \
     ' word in this string'
words = st100.split()
for char in words:
    first_char = char[0]
    print(list(first_char))

#list comprehension example:
mystring = 'Create a list of the first letters of every' \
           ' word in this string'
[word[0] for word in mystring.split()]
print(mystring)
