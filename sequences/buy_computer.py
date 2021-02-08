current_choice = "-"
computer_parts = []

while current_choice != '0':
    if current_choice in "123456":
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

    else:
        print("Please add from below:")
        print("1: computer")
        print("2: monitor")
        print("3: motherboard")
        print("4: mouse")
        print("5: speakers")
        print("6: hdmi cable")
        print("0: Finish shopping")

    current_choice = input()
print("You are buying {}".format(computer_parts))