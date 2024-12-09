ok_input = False
hours = None
rate = None

while ok_input == False:
    try:
        hours = input("How many hours did you work? ")
        hours = float(hours)
        ok_input = True
    except:
        print("Please enter a valid number\n")

ok_input = False
while ok_input == False:
    try:
        rate = input("How much do you get paid per normal hour? ")
        rate = float(rate)
        ok_input = True
    except:
        print("Please enter a valid number\n")
        
if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * (rate * 1.5)

print("Your pay is", pay)
