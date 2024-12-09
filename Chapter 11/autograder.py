import re

fname = input("Filename: ")
try :
    fhand = open(fname, "r")
except :
    print("Cannot open file or directory:", fname)

# python generators / list comprehension
print(sum([int(number) for number in re.findall('[0-9]+', fhand.read())]))

# the more verbose way

# summ = 0
# 
# for line in fhand :
#     line.rstrip()
#     numbers = re.findall("[0-9]+", line)
#     for number in numbers :
#         summ += int(number)
# 
# print(summ)