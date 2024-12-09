name = input("Filename: ")
if len(name) < 1 :
    name = "mbox-short.txt"
fhand = open(name)

hours = dict()

for line in fhand :
    if line.startswith("From") :
        words = line.split()
        if len(words) < 6 : continue
        hour = words[5].split(":")
        hours[hour[0]] = hours.get(hour[0], 0) + 1
        
l = sorted([(h, c) for h, c in hours.items()])

for h, c in l :
    print(h, c)