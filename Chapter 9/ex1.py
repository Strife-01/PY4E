fhand = open("words.txt")

di = dict()

for line in fhand :
    line.rstrip()
    words = line.split(" ")
    for word in words :
        if word not in di : di[word] = "exists"

w = input("Search a word: ")
try :
    print(di[w])
except :
    print("the word is not in the file...")
