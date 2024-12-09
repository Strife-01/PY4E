# get the file name
fname = input("File name: ")

#open the file
try:
    fhandle = open(fname, 'r')
except:
    print("Invalid file name...")
    quit()

# iterate through each line and print it uppercase
for line in fhandle:
    print(line[:len(line)-1].upper())

fhandle.close()