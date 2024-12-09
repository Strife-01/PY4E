# declare the variables needed

user_input = None
largest_number = None
smallest_number = None

# get the user input

while user_input != 'done':
    if user_input == 'done':
        break

    if user_input is None:
        user_input = input("enter a number or done: ")
        try:
            user_input = int(user_input)
            largest_number = user_input
            smallest_number = user_input
        except:
            if user_input != 'done':
                print("Invalid input\n")
    else:
        user_input = input("enter a number or done: ")
        try:
            user_input = int(user_input)
            if user_input > largest_number:
                largest_number = user_input
            if user_input < smallest_number:
                smallest_number = user_input
        except:
            if user_input != 'done':
                print("Invalid input\n")


# print the largest number

print("Maximum is", largest_number)
print("Minimum is", smallest_number)
