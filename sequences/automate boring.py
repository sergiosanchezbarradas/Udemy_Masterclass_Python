# This program says hello and asks for my name.
print('Hello, world!')
print('Whats your name')
your_name = input()
print('nice to meet you ' + your_name)

length_name = (len(your_name))
print('your name is {} characters long'.format(length_name))

print("What's your age")
age = input()
print("You will be " + str(int(age)+1) + " next year.....old fella")

#Casting
#If you want to specify the data type of a variable, this can be done with casting.

#Example
#x = str(3)    # x will be '3'
#y = int(3)    # y will be 3
#z = float(3)  # z will be 3.0