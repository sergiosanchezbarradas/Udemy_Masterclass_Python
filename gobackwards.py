data = [104, 101, 4, 105, 308, 103, 5,
        107, 100, 306, 106, 102, 108]
min = 100
max = 200

# for index in range(len(data) -1, -1, -1):
#     if data[index] < min or data[index] > max:
#         print(index, data)
#         del data[index]
#
# print(data)

# print in reverse
#
# top_index = len(data) - 1
# for index, value in enumerate(reversed(data)):
#     print(top_index - index, value)
#
# # print(data)
#
# top_index = len(data) - 1
# for index, value in enumerate(data):
#     print(top_index - index, value)

#if you want to remove certain values

top_index = len(data) - 1
for index, value in enumerate(reversed(data)):
    if value < min or value > max:
        print(top_index - index, value)
        del data[top_index - index]

print(data)