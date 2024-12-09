numbers = list()

while True:
    user_input = input("Enter a number or done: ")
    if user_input.lower() == "done": break
    try:
        number = float(user_input)
        numbers.append(number)
    except:
        print("Enter a valid number or done...")

try:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
except:
    print("No elements in the list...")
