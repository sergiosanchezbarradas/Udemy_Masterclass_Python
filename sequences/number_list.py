empty_list = []
even = [2, 4, 6, 8]
odd = [1, 3, 5, 7, 9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)

digits = list("44534535622345")
print(digits)
print(sorted(digits))
print()
more_numbers = list(numbers)
print(more_numbers)
print(more_numbers == numbers)
print(numbers is more_numbers)

