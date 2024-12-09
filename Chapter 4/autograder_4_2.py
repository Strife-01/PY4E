score = None
ok_input = False

def computergrade(score):
    if score < 0.0 or score > 1.0:
        return "Out of range\n"
    else:
        if score < 0.6:
            return "F"
        elif score < 0.7:
            return "D"
        elif score < 0.8:
            return "C"
        elif score < 0.9:
            return "B"
        else:
            return "A"

while ok_input == False:
    try:
        score = input("Please enter a score: ")
        score = float(score)
        ok_input = True
    except:
        print("Please enter a number...\n")

print(computergrade(score))
