# ask the user for a file to open
# fname = input("Filename... ")

fname = "mbox-short.txt"

# open the file 
try:
    fhand = open(fname, 'r')
except:
    print("no such file:", fsname)
    quit()

# parse the file line by line and print the address
count = 0

for line in fhand:
    if not line.startswith("From:"):
        continue
    else:
        count += 1
        words = line.split()
        print(words[1])

# print the count
print("There were", count, "lines in the file with From as the first word\n")

