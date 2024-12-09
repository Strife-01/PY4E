import urllib.request

URL = 'http://data.pr4e.org/romeo.txt'
fhand = urllib.request.urlopen(URL)
# for line in fhand :
#     print(line.decode().strip())

counts = dict()
for line in fhand :
    words = line.decode().split()
    for word in words :
        counts[word] = counts.get(word, 0) + 1

print(counts)
