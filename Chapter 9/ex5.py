fhand = open("mbox-short.txt")

di = dict()

for line in fhand :
    if line.startswith("From") :
        line.strip()
        words = line.split()
        if len(words) == 2 :
            address = words[1].split('@')
            di[address[1]] = di.get(address[1], 0) + 1

print(di)
