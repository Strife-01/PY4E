# ask the user which file to open and then open it
fname = input("Filemane: ")
try:
    file_pointer = open(fname, 'r')
except:
    print("Invalid file name: ", fname)

# variables needed for the output
appearances = 0
average = 0

# parse the file line by line
for line in file_pointer:
    if 'X-DSPAM-Confidence:' in line:
        collon = line.find(':')
        new_line = line.find('\n')
        average += float(line[collon + 1 : new_line].strip())
        appearances += 1

# close the file
file_pointer.close()

# print the average
print("Average spam confidence:", average / appearances)
