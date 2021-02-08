available_parts = ["computer",
                   "monitor",
                   "motherboard",
                   "mouse",
                   "speakers",
                   "hdmi cable",
                   "dvd drive"
                   ]
current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "1234567":
        print("Adding {}".format(current_choice))
        if current_choice == '1':
            computer_parts.append("computer")
        elif current_choice == '2':
            computer_parts.append("monitor")
        elif current_choice == '3':
            computer_parts.append("motherboard")
        elif current_choice == '4':
            computer_parts.append("mouse")
        elif current_choice == '5':
            computer_parts.append("speakers")
        elif current_choice == '6':
            computer_parts.append("hdmi cable")
        elif current_choice == '7':
            computer_parts.append("tacos al pastor")

    else:
        print("Please add from below:")
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part)+ 1, part))  #not most effcient as python has to search each party
        #Better code:
        for number, part in enumerate(available_parts):
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()
print("You are buying {}".format(computer_parts))