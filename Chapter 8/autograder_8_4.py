# ask the user for a file to open
fname = input("Filename:... ")

# open the file
try:
    fhand = open(fname, "r")
except:
    print("No such file found with the name", fname)

# create an empty list
words = list()

# parse the file and populate the words list
for line in fhand:
    line_list = line.split()
    # add the words inside the words list
    for word in range(len(line_list)):
        # add it if the word is not on the list
        found = False
        for w in range(len(words)):
            if words[w] == line_list[word]:
                found = True
                break
        if found == False:
            words.append(line_list[word])
# sort the list and print it
words.sort()

print(words)
