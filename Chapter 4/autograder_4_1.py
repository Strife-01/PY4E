def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    return 40 * rate + (hours - 40) * (rate * 1.5);

ishours = False
while ishours == False:
    hours = input("How many hours did you work? ")
    try:
        hours = float(hours)
        ishours = True
    except:
        print("Please enter a valid number\n")

israte = False
while israte == False:
    rate = input("What is your normal hourly rate? ")
    try:
        rate = float(rate)
        israte = True
    except:
        print("Please enter a valid number\n")

pay = computepay(hours, rate)
print("Your pay is", pay)
