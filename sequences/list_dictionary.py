author = {"name":"Sergio",
          "color":"orange",
          "shape":"square"
          }
#color list
colors = ["blue", "orange", "green", "naranja"]

print("The author's name is {}".format(author["name"]))
print("fav color is {}".format(author["color"]))
print()
#show what color we have
print("Colors available are:")
for color in colors:
    print(color)

#Ask fav color
new_color = input("What's your fav color? ")
if new_color == author["color"]:
     print("We like the same color")

#add color to list if it is new
if new_color not in colors:
    print("Adding this to the list, thanks for mentioning it")
    colors.append(new_color)
    #print message
    message = ("We have {} colors in the list." .format(len(colors)))
    message += "Added color was {}.".format(color[4])
    print(message)
    print(colors)
else:
    pass