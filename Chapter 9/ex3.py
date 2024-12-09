fhand = open("mbox-short.txt")

di = dict()

for line in fhand :
    if line.startswith("From") :
        line.strip()
        words = line.split()
        if len(words) == 2 :
            di[words[1]] = di.get(words[1], 0) + 1

print(di)
