fname = input("Filename: ")
if len(fname) < 1 : fhand = open("mbox-short.txt")
else :
    try :
        fhand = open(fname)
    except :
        print("No such file in this directory...")

di = dict()

for line in fhand :
    if line.startswith("From") : 
        line.rstrip()
        words = line.split()
        if len(words) is 2 : di[words[1]] = di.get(words[1], 0) + 1;

max_address = None
max_messages = None
for address, appearances in di.items() :
    if max_address == None and max_messages == None :
        max_address = address
        max_messages = appearances
    else :
        if appearances > max_messages :
            max_address = address
            max_messages = appearances

print(max_address, max_messages)
