fname = "mbox-short.txt"
fhand = open(fname)

d = dict()

for line in fhand :
    if line.startswith("From:") :
        line.rstrip()
        words = line.split()
        d[words[1]] = d.get(words[1], 0) + 1

sorted_list = sorted([(nr, address) for address, nr in d.items()], reverse=True)
print(sorted_list[0][1], sorted_list[0][0])