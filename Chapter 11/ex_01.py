import re

file_name = input("Filename: ")
try :
    fhand = open(file_name, "r")
except :
    print("Couldn't open file ", file_name)

regex = input("Enter a regular expression: ")

# parse the file and look for the regex

nr_lines = 0

for line in fhand :
    line.rstrip()
    if re.search(regex, line) : nr_lines += 1

print(file_name, "had", nr_lines, "lines that had matched ", regex)

