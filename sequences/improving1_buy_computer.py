available_parts = ["computer",
                   "monitor",
                   "motherboard",
                   "mouse",
                   "speakers",
                   "hdmi cable",
                   "dvd drive",
                   "tacos"
                   ]
# not best code:
# valid_choices = [str(i) for i in range(1, len(available_parts) +1)]
# improving line 10:
valid_choices = []
for i in range(1, len(available_parts) +1):
    valid_choices.append(str(i))
print(valid_choices)

current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in valid_choices:
        print("Adding {}".format(current_choice))
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        computer_parts.append(chosen_part)

    else:
        print("Please add from below:")
        # for part in available_parts:
        #   print("{0}: {1}".format(available_parts.index(part)+ 1, part))  #not most effcient as python has to search each party

        #Better code:
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()
print("You are buying {}".format(computer_parts))