fhand = open("mbox-short.txt")

di = dict()

for line in fhand :
    if line.startswith("From") :
        line.strip()
        words = line.split()
        if len(words) >= 3 :
            di[words[2]] = di.get(words[2], 0) + 1

print(di)
