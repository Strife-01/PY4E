#fname = input("Filename: ")

fhand = open("mbox-short.txt")

d = dict()

for line in fhand :
    words = line.split()
    for word in words :
        for letter in word :
            if letter >= 'a' and letter <= 'z' :
                d[letter] = d.get(letter, 0) + 1
            elif letter >= 'A' and letter <= 'Z' :
                letter = letter.lower()
                d[letter] = d.get(letter, 0) + 1

letters = sorted([(c, l) for (l, c) in d.items()], reverse=True)

for (c, l) in letters :
    print(l, c)