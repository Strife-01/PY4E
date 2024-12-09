# take input from user
hours = input("How many hours did you work? ")
rate = input("How much do you make per hour? ")

# convert the input into floating point numbers and calculate their pay
pay = float(hours) * float(rate)

#print the pay to the stdout
print("You will be paid:", pay)
