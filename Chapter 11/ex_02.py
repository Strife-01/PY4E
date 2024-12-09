import re

fname = input("Filename: ")

try :
    fhand = open(fname, "r")
except :
    print("No such file or directory", fname)
    quit()

average = 0
nrs = 0

for line in fhand :
    line.rstrip()
    numbers = re.findall('New Revision: ([0-9]+)', line)
    for number in numbers :
        try :
            number = float(number)
            average += number
            nrs += 1
        except : continue

average = int(average / nrs)
print(average)
