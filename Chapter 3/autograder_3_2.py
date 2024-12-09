score = None
ok_input = False

while ok_input == False:
    try:
        score = input("Please enter a score: ")
        score = float(score)
        ok_input = True
    except:
        print("Please enter a number...\n")

if score < 0.0 or score > 1.0:
    print("Out of range\n")
else:
    if score < 0.6:
        print("< 0.6 F")
    elif score < 0.7:
        print(">= 0.6 D")
    elif score < 0.8:
        print(">= 0.7 C")
    elif score < 0.9:
        print(">= 0.8 B")
    else:
        print(">= 0.9 A")
