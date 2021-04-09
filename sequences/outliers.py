data = [4, 5, 123, 434, 123, 234234, 43562356,
        456, 6534, 35734, 5673, 69809]

minvalue = 1000
maxvalue = 100000

# process low values from the list
stop = 0
for index, value in enumerate(data):
    if value >= minvalue:
        stop = index
        break

print(stop)  # for debugging
del data[:stop]
print(data)
